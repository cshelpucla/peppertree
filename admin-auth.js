/**
 * Admin Authentication System
 * Handles login modal, user management, and session management
 */

// Check authentication on page load
let currentUser = null;

async function checkAuth() {
    try {
        const response = await fetch('auth.php');
        const data = await response.json();
        
        if (data.authenticated) {
            currentUser = data.user;
            showLoggedInState();
            showApplicationsLink();
        } else {
            currentUser = null;
            showSignInState();
            hideApplicationsLink();
        }
    } catch (error) {
        console.error('Auth check failed:', error);
        showSignInState();
        hideApplicationsLink();
    }
}

function showSignInState() {
    const authLink = document.getElementById('authNavLink');
    if (authLink) {
        authLink.textContent = 'Sign In';
        authLink.classList.remove('logged-in');
        authLink.onclick = (e) => {
            e.preventDefault();
            openLoginModal();
        };
    }
}

function showLoggedInState() {
    const authLink = document.getElementById('authNavLink');
    if (authLink) {
        authLink.textContent = `👤 ${currentUser.username}`;
        authLink.classList.add('logged-in');
        authLink.onclick = (e) => {
            e.preventDefault();
            openAdminMenu();
        };
    }
}

function showApplicationsLink() {
    const applicationsLinks = document.querySelectorAll('a[href="applications-list.html"]');
    applicationsLinks.forEach(link => {
        link.style.display = 'inline-block';
        link.style.setProperty('display', 'inline-block', 'important');
    });
}

function hideApplicationsLink() {
    const applicationsLinks = document.querySelectorAll('a[href="applications-list.html"]');
    applicationsLinks.forEach(link => {
        link.style.setProperty('display', 'none', 'important');
    });
}

// Login Modal
function openLoginModal() {
    const modal = document.getElementById('loginModal');
    if (modal) {
        modal.style.display = 'flex';
        document.getElementById('loginUsername').value = '';
        document.getElementById('loginPassword').value = '';
        document.getElementById('loginError').style.display = 'none';
    }
}

function closeLoginModal() {
    const modal = document.getElementById('loginModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

async function handleLogin(event) {
    event.preventDefault();
    
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;
    const errorDiv = document.getElementById('loginError');
    
    try {
        const response = await fetch('auth.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        
        const data = await response.json();
        
        if (data.success) {
            currentUser = data.user;
            closeLoginModal();
            showLoggedInState();
            showApplicationsLink();
            showNotification('Logged in successfully!', 'success');
        } else {
            errorDiv.textContent = data.message || 'Invalid credentials';
            errorDiv.style.display = 'block';
        }
    } catch (error) {
        errorDiv.textContent = 'Login failed. Please try again.';
        errorDiv.style.display = 'block';
    }
}

async function handleLogout() {
    try {
        await fetch('auth.php', { method: 'DELETE' });
        currentUser = null;
        showSignInState();
        hideApplicationsLink();
        closeAdminMenu();
        showNotification('Logged out successfully', 'success');
    } catch (error) {
        console.error('Logout failed:', error);
    }
}

// Admin Menu
function openAdminMenu() {
    const menu = document.getElementById('adminMenu');
    if (menu) {
        menu.style.display = 'block';
    }
}

function closeAdminMenu() {
    const menu = document.getElementById('adminMenu');
    if (menu) {
        menu.style.display = 'none';
    }
}

// User Management Modal
async function openUserManagement() {
    closeAdminMenu();
    const modal = document.getElementById('userManagementModal');
    if (modal) {
        modal.style.display = 'flex';
        await loadUsers();
    }
}

function closeUserManagement() {
    const modal = document.getElementById('userManagementModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

async function loadUsers() {
    try {
        const response = await fetch('manage_users.php');
        const data = await response.json();
        
        if (data.success) {
            renderUsersList(data.users);
        }
    } catch (error) {
        console.error('Failed to load users:', error);
    }
}

function renderUsersList(users) {
    const tbody = document.getElementById('usersTableBody');
    tbody.innerHTML = '';
    
    users.forEach(user => {
        const tr = document.createElement('tr');
        const lastLogin = user.lastLogin ? new Date(user.lastLogin).toLocaleString() : 'Never';
        const createdAt = new Date(user.createdAt).toLocaleDateString();
        
        tr.innerHTML = `
            <td>${user.username}</td>
            <td>${user.email}</td>
            <td><span class="role-badge role-${user.role}">${user.role}</span></td>
            <td>${createdAt}</td>
            <td>${lastLogin}</td>
            <td>
                ${user.id !== currentUser.id ? 
                    `<button class="btn-delete" onclick="deleteUser('${user.id}', '${user.username}')">🗑️ Delete</button>` : 
                    '<span style="color: #999;">Current User</span>'}
            </td>
        `;
        tbody.appendChild(tr);
    });
}

// Add User Modal
function openAddUserModal() {
    const modal = document.getElementById('addUserModal');
    if (modal) {
        modal.style.display = 'flex';
        document.getElementById('addUserForm').reset();
        document.getElementById('addUserError').style.display = 'none';
    }
}

function closeAddUserModal() {
    const modal = document.getElementById('addUserModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

async function handleAddUser(event) {
    event.preventDefault();
    
    const username = document.getElementById('newUsername').value;
    const email = document.getElementById('newEmail').value;
    const password = document.getElementById('newPassword').value;
    const role = document.getElementById('newRole').value;
    const errorDiv = document.getElementById('addUserError');
    
    try {
        const response = await fetch('manage_users.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, email, password, role })
        });
        
        const data = await response.json();
        
        if (data.success) {
            closeAddUserModal();
            await loadUsers();
            showNotification('User added successfully!', 'success');
        } else {
            errorDiv.textContent = data.message || 'Failed to add user';
            errorDiv.style.display = 'block';
        }
    } catch (error) {
        errorDiv.textContent = 'Failed to add user. Please try again.';
        errorDiv.style.display = 'block';
    }
}

async function deleteUser(userId, username) {
    if (!confirm(`Are you sure you want to delete user "${username}"?`)) {
        return;
    }
    
    try {
        const response = await fetch(`manage_users.php?id=${userId}`, {
            method: 'DELETE'
        });
        
        const data = await response.json();
        
        if (data.success) {
            await loadUsers();
            showNotification('User deleted successfully', 'success');
        } else {
            showNotification(data.message || 'Failed to delete user', 'error');
        }
    } catch (error) {
        showNotification('Failed to delete user', 'error');
    }
}

// Notification system
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.classList.add('show');
    }, 10);
    
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Close modals on outside click
window.onclick = function(event) {
    const loginModal = document.getElementById('loginModal');
    const userMgmtModal = document.getElementById('userManagementModal');
    const addUserModal = document.getElementById('addUserModal');
    const adminMenu = document.getElementById('adminMenu');
    
    if (event.target === loginModal) {
        closeLoginModal();
    }
    if (event.target === userMgmtModal) {
        closeUserManagement();
    }
    if (event.target === addUserModal) {
        closeAddUserModal();
    }
    if (adminMenu && !event.target.closest('#adminMenu') && !event.target.closest('#authNavLink')) {
        closeAdminMenu();
    }
};

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    checkAuth();
});
