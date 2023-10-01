if(!localStorage.getItem('counter')){
  localStorage.setItem('counter', 0);
}


function count() {
  let counter = localStorage.getItem('counter');
  counter++;
  localStorage.setItem('counter', counter);
  document.querySelector('h2').innerHTML = 'Count: ' + counter;

  if (counter % 10 === 0) {
    alert(`Count is now ${counter}`); 
  }
}

document.addEventListener('DOMContentLoaded', function() {
  
  let counter = localStorage.getItem('counter');
  document.querySelector('h2').innerHTML = 'Count: ' + counter;

  document.querySelector('button').onclick = count; 
  
  // setInterval(count, 1000);
})