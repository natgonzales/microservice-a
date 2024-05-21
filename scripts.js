// displays most recently uploaded image

function uploadImage() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select an image to upload.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (data.filename) {
            displayImage(data.filename); // calls displayImage()
        }
        fileInput.value = ''; // Clear the file input after upload
    })
    .catch(error => {
        console.error('Error uploading image:', error);
        alert('Error uploading image. Please try again.');
    });
}

function displayImage(imageName) {
    const imageContainer = document.getElementById('imageContainer');
    const img = document.createElement('img');
    img.src = `http://127.0.0.1:5000/images/${imageName}`;
    img.alt = imageName;
    img.style.maxWidth = '100%'; // fit in container
    imageContainer.innerHTML = ''; // Clear previous images
    imageContainer.appendChild(img);
}
