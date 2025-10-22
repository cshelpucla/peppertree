// Video Modal Functions

function openVideoModal(videoSrc, title) {
    const modal = document.getElementById('videoModal');
    const video = document.getElementById('modalVideo');
    const source = video.querySelector('source');
    const titleElement = document.getElementById('videoModalTitle');
    
    // Set video source
    source.src = videoSrc;
    video.load();
    
    // Set title
    if (titleElement && title) {
        titleElement.textContent = title;
    }
    
    // Show modal
    modal.classList.add('active');
    
    // Play video
    video.play();
    
    // Prevent body scroll
    document.body.style.overflow = 'hidden';
}

function closeVideoModal() {
    const modal = document.getElementById('videoModal');
    const video = document.getElementById('modalVideo');
    
    // Pause and reset video
    video.pause();
    video.currentTime = 0;
    
    // Hide modal
    modal.classList.remove('active');
    
    // Restore body scroll
    document.body.style.overflow = '';
}

// Close modal when clicking outside the video
document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('videoModal');
    
    if (modal) {
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                closeVideoModal();
            }
        });
    }
});

// Close modal with Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        const modal = document.getElementById('videoModal');
        if (modal && modal.classList.contains('active')) {
            closeVideoModal();
        }
    }
});
