// Define the relative path or resource path of your API endpoint
const apiEndpoint = '/myendpoint';

// Function to submit user data to the backend Lambda function
function submitUserData(userData) {
    fetch(apiEndpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        // Handle the response data
        console.log(data);
    })
    .catch(error => {
        // Handle errors
        console.error('There was a problem with the fetch operation:', error);
    });
}

// Example usage: Submit user data
const userData = {
    firstName: 'John',
    lastName: 'Doe'
};
submitUserData(userData);

