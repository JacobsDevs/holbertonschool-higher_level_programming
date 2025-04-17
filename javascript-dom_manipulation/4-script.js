const adder = document.querySelector('#add_item');
const list = document.querySelector('ul')
adder.addEventListener('click', () => {
  const li = document.createElement('li');
  li.innerText = 'Item';
  list.appendChild(li)
});
