function previewImage(inputId, previewId) {
    const fileInput = document.getElementById(inputId);
    const preview = document.getElementById(previewId);
    const file = fileInput.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
}

document.getElementById('user-image').addEventListener('change', () => {
    previewImage('user-image', 'user-preview');
});

document.getElementById('character-image').addEventListener('change', () => {
    previewImage('character-image', 'character-preview');
});

document.getElementById('generate-btn').addEventListener('click', async () => {
    const userImage = document.getElementById('user-image').files[0];
    const characterImage = document.getElementById('character-image').files[0];
    const promptText = document.getElementById('prompt').value;

    if (!userImage || !characterImage) {
        alert('Please upload both images.');
        return;
    }

    const formData = new FormData();
    formData.append('user_image', userImage);
    formData.append('character_image', characterImage);
    formData.append('prompt', promptText);

    document.getElementById('loading').style.display = 'block';
    document.getElementById('result').innerHTML = '';

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            body: formData
        });

        const imageUrl = await response.text(); // or .json() if needed
        document.getElementById('result').innerHTML = `<img src="${imageUrl}" alt="Result Image">`;
    } catch (error) {
        console.error('Error:', error);
        alert('Something went wrong. Please try again.');
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
});
