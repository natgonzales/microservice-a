# Image Server

## Description

This is a microservice for CS361. It allows simple image upload and retrieval using a Flask backend. Users can also retrieve and display images on a web interface.

## Communication Contract

### Requesting Data

To request data from the microservice, you can use an HTTP POST request to upload an image, or an HTTP GET request to retrieve an image. 

To upload an image, create a form data object to hold the image file. Then, send a POST request to the /upload endpoint of the microservice with the form data containing the image file attached. 

To retrive an image, specify the image's file name, and send a GET request to the /images/<filename> endpoint of the microservice. Replace <filename> with the actual file name of the image.

#### Example Call
This is an example call using JavaScript with Fetch API.

```javascript
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
```

### Receiving Data

Receiving data from the microservices involves how the server is handling the HTTP requests.

For the get image request, the microservice will respond with the image file if it exists. It will be sent using Flask's send_file() function. The image can be displayed by setting the src attribute of an image element to the URL of the retrieved image. 

#### Example Call
The responses are already integrated in the Flask app.

Below are the responses for the upload route:
```javascript
function displayImage(imageName) {
    const imageContainer = document.getElementById('imageContainer');
    const img = document.createElement('img');
    img.src = `http://127.0.0.1:5000/images/${imageName}`;
    img.alt = imageName;
    img.style.maxWidth = '100%'; // fit in container
    imageContainer.innerHTML = ''; // Clear previous images
    imageContainer.appendChild(img);
}
```

