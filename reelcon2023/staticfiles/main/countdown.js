function updateCountdown() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/countdown/api/', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.time_remaining) {
                document.getElementById('countdown').innerHTML = 'Time remaining: ' + response.time_remaining;
            } else {
                document.getElementById('countdown').innerHTML = 'No countdown set.';
            }
        }
    };
    xhr.send();
}

// Update the countdown every second
setInterval(updateCountdown, 1000);