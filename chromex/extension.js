const h1Tag = document.getElementById('currentUrl');




// onclick Function for the button to create an event for the further process
document.getElementById('click')?.addEventListener('click', function() {
  // Fetching the current chrome tab url to pass to the flask api
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      var currentUrl = tabs[0].url;
      // sending request to the flask server & passed the url to the server
      fetch("http://localhost:5000/CheckPhishing", {
          method: 'POST',
          body: JSON.stringify({ url: currentUrl }), // Include data in the request body
          headers: {
              'Content-Type': 'application/json' // Set the content type to JSON
          }
      }).then(
          result => {
              return result.json();
          }
      ).then(
          data => {
            // adding the result to the popup tab
              h1Tag.innerText = data["result"];
          }
      ).catch(error => {
          console.error('Error:', error);
      });
  });
});