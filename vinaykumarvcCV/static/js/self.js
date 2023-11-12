let allTabsValues = new Map();
getResponseForURI('/experience')
    .then(apiResponseHTML => {
        allTabsValues.set('experience', apiResponseHTML);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
getResponseForURI('/education')
    .then(apiResponseHTML => {
        allTabsValues.set('education', apiResponseHTML);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });

getResponseForURI('/projects')
    .then(apiResponseHTML => {
        allTabsValues.set('projects', apiResponseHTML);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });

getResponseForURI('/skills')
    .then(apiResponseHTML => {
        allTabsValues.set('skills', apiResponseHTML);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });

function getResponseForURI(apiUrl) {
    return new Promise((resolve, reject) => {
        fetch(apiUrl)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.text();
            })
            .then(htmlContent => {
                resolve(htmlContent);
            })
            .catch(error => {
                reject(error);
            });
    });
}

function switchTabs(id) {
    let targetElement = document.getElementById('details_common_content');
    targetElement.innerHTML = allTabsValues.get(id)
}





