// // https://api.openweathermap.org/data/2.5/weather?q=canada&appid=f49ebbb8cbf67059d91c88a1f97ddfa9
// async function fetchWeatherData(location) {
//     const apiKey = weather_api_key; // Use the globally available API key
//     const url = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}&units=metric`;
//     try {
//         const response = await fetch(url);
//         if (!response.ok) {
//             throw new Error('Network response was not ok ' + response.statusText);
//         }
//         const data = await response.json();
//         return data;
//     }
//     catch (error) {
//         console.error('There has been a problem with your fetch operation:', error);
//     }
// }
// console.log(fetchWeatherData(user_location)); // Use the globally available user location