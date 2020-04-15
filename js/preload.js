console.log('Preload Script Injected!');

window.addEventListener('DOMContentLoaded', () => {
    console.log('Running Preload');

    var greenChart = document.createElement('style');
    greenChart.innerText = '#chart { background-color: green; }';

    document.head.append(greenChart);
});