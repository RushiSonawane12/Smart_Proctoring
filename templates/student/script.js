async function detectFaces() {
    // Get the video element
    const video = document.getElementById('video');

    try {
      // Request access to the user's camera
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });

      // Set the video source to the camera stream
      video.srcObject = stream;

      // Wait for the video to start playing
      await new Promise(resolve => video.addEventListener('canplaythrough', resolve, { once: true }));

      // Get the video's dimensions
      const width = video.videoWidth;
      const height = video.videoHeight;

      // Create a canvas to draw the video on
      const canvas = document.createElement('canvas');
      canvas.width = width;
      canvas.height = height;
      const ctx = canvas.getContext('2d');

      // Draw the video on the canvas
      function drawVideo() {
        ctx.drawImage(video, 0, 0, width, height);
        requestAnimationFrame(drawVideo);
      }
      drawVideo();

      // Detect faces in the canvas
      const faceDetector = new FaceDetector();
      const faces = await faceDetector.detect(canvas);

      // If there are two or more faces, trigger an alert
      if (faces.length >= 2) {
        alert('Two or more people detected!');
      }
    } catch (error) {
      console.error('Error accessing camera:', error);
    }
  }

  // Start the face detection loop
  detectFaces();

