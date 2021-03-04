const alerts = document.querySelector('#notification');

// Add is-active class to current selected menu
const currentLocation = location.href;
const menuItem = document.querySelectorAll('a');
const currentItem = document.querySelector('.is-active');
const length = menuItem.length;

for (let i = 0; i < length; i++) {
  if (menuItem[i].href === currentLocation) {
    currentItem?.classList.remove('is-active');
    menuItem[i].classList.add('is-active');
  }
}

// Hide Alert Messages after 4 seconds
setTimeout(() => {
  if (alerts) {
    alerts.style.display = 'None';
  }
}, 4000);

// Login form -- Improve
// const loginEmail = document.querySelector('#login_email');
// const controlElement = loginEmail.parentElement;
// console.log(loginEmail.parentElement.parentElement);
// loginEmail.addEventListener('input', (e) => {
//   let html = `<div class="field">
//   <div class="control">
//   <input class="input danger">
//   <div class="has-text-weight-light has-text-danger">NOt correct</div>
//   </div>`;
//   if (e.target.value === 'amin@gmail.com') {
//     console.log('Correct');
//     loginEmail.classList.remove('is-danger');
//     loginEmail.classList.add('is-success');
//     const div = `<div class="has-text-weight-light has-text-sucess">Correct</div>`;
//     controlElement.innerHTML += div;
//   } else {
//     console.log(e.target.value);
//     loginEmail.classList.add('is-danger');
//     const div = `<div class="has-text-weight-light has-text-danger">Not correct</div>`;
//     controlElement.innerHTML += div;
//   }
// });
