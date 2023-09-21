const dropArea = document.getElementById('dropArea');
const submitBtn = document.getElementById('submitBtn');

// Prevent default behavior for drag-and-drop events
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

// Highlight drop area when a file is dragged over it
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false);
});

['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false);
});

function highlight(e) {
    dropArea.classList.add('highlight');
}

function unhighlight(e) {
    dropArea.classList.remove('highlight');
}

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false);

function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;

    handleFiles(files);
}

function handleFiles(files) {
    for (const file of files) {
        const reader = new FileReader();

        reader.onload = function() {
            const img = new Image();
            img.src = reader.result;

            document.body.appendChild(img);
        }

        reader.readAsDataURL(file);
    }
}

submitBtn.addEventListener('click', function() {
    const files = document.getElementById('fileInput').files;
    handleFiles(files);
    // Redirect the user to a new page (e.g., "newpage.html")
    window.location.href = 'response.html';
});