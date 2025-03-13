const getMarkets = async () => {
    const response = await fetch('/markets');
    const data = await response.json();
    return data;
};

const createMarketOptions = (markets) => {
    const marketSelect = document.getElementById('market');
    markets.forEach((market) => {
        const option = document.createElement('option');
        option.value = market.id;
        option.text = market.market;
        marketSelect.appendChild(option);
    });
};

window.addEventListener("load", (e) => {
    getMarkets().then((markets) => {
        createMarketOptions(markets);
        const marketSelect = document.getElementById('market');
        new Choices(marketSelect, { placeholder: true });
    });
});

const verifyDates = () => {
    const startMonth = document.getElementById('start_month').value;
    const startYear = document.getElementById('start_year').value;
    const endMonth = document.getElementById('end_month').value;
    const endYear = document.getElementById('end_year').value;

    if (startYear > endYear || (startYear == endYear && startMonth > endMonth)) {
        alert('Invalid date range');
        return false;
    }

    if (startMonth && !startYear) {
        alert('Start year must be set');
        return false;
    }

    if (endMonth && !endYear) {
        alert('End year must be set');
        return false;
    }

    if (startMonth && !endMonth || !startMonth && endMonth || startYear && !endYear || !startYear && endYear) {
        alert('Start and end date must be set');
        return false;
    }

    return true;
}

const getFlights = async (marketId, startMonth, startYear, endMonth, endYear) => {
    const url = `/flights?market_id=${marketId}&start_month=${startMonth}&start_year=${startYear}&end_month=${endMonth}&end_year=${endYear}`;
    const response = await fetch(url);
    const data = await response.json();
    return data;
}

const generateChartData = (data, includeNull) => {
    dates = [];
    rpks = [];

    for (const flight of data) {
        if (!includeNull && flight.rpk == null) {
            continue;
        }
        if (flight.rpk == null) {
            flight.rpk = 0;
        }
        date = new Date(flight.year, flight.month, 1)
        dates.push(date);
        rpks.push(flight.rpk);
    }

    return [dates, rpks];
}

const generateChart = (dates, rpks, marketName) => {
    const trace = {
        x: dates,
        y: rpks,
        mode: 'markers',
        type: 'scatter',
        name: 'RPKs Over Time'
    };

    const layout = {
        title: 'RPKs Over Time',
        xaxis: {
            title: 'Date',
            tickformat: '%Y-%m'
        },
        yaxis: {
            title: 'Number'
        }
    };

    document.getElementById('chart').innerHTML = '';
    Plotly.newPlot('chart', [trace], layout);
};

const updateChartTitle = (marketName) => {
    document.getElementById('chart_title').innerText = `RPKs Over Time for ${marketName}`;
}

document.getElementById('dashboard-form').onsubmit = (e) => {
    e.preventDefault();

    const marketId = document.getElementById('market').value;
    const marketName = document.getElementById('market').options[document.getElementById('market').selectedIndex].text;
    const startMonth = document.getElementById('start_month').value;
    const startYear = document.getElementById('start_year').value;
    const endMonth = document.getElementById('end_month').value;
    const endYear = document.getElementById('end_year').value;
    const includeNull = document.getElementById('include_null').checked;

    if (!verifyDates()) {
        return
    }

    getFlights(marketId, startMonth, startYear, endMonth, endYear).then((data) => {
        if (data.length == 0) {
            alert('No data found');
            return;
        }
        const [dates, rpks] = generateChartData(data, includeNull);
        generateChart(dates, rpks, marketName);
        updateChartTitle(marketName);
    });
};