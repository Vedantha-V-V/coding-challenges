let dateContainer = document.getElementById("date")
let rightSection = document.getElementById("right-section")
let leftSection = document.getElementById("left-section")

// dateContainer.textContent ="14:47"
console.log(dateContainer.innerText)
// Get the date element update it every one second

async function requestData(){
    const response = await fetch("https://codingchallenges.substack.com/feed")
    console.log(response)
}

function showChallenges(){

}

function showPulls(){

}

requestData();

// 
// https://api.github.com/repositories/692739619/pulls