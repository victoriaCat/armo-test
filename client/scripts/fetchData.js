const ipc = require('electron').ipcRenderer;
const axios = require('axios');
function fetchData(){
    axios.get('http://localhost:8888')
        .then(response => {
            let res = response.data;
            let output = '';
            res.forEach((item) => {
                output += `
                <li class="list-item">${item.prop}</li>`
            })
            document.getElementById('list').innerHTML = output;
        })
        .catch(error => {
            console.log(error);
        });
}