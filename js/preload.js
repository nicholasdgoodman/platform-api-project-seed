console.log('Preload Script Injected!');

window.addEventListener('DOMContentLoaded', () => {
    console.log('Running Preload');

    var greenChart = document.createElement('style');
    greenChart.innerText = '#chart { background-color: green; }';

    document.head.append(greenChart);

    console.log(window.location.origin);
    if(window.location.origin == 'https://www.nasdaq.com') {
        console.log('Running on NASDAQ');
        fin.InterApplicationBus.subscribe({ uuid: '*' }, 'ticker-change', ticker => {
            console.log('ticker change event, navigating...');
            location.href = ticker;
        });
    }
});