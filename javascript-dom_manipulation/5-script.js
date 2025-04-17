const header = document.querySelector('header');
const updater = document.querySelector('#update_header')
updater.addEventListener('click', () => {
  header.innerText = 'New Header!!!';
});
