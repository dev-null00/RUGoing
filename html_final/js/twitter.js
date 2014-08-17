function runtwitter(eventTitle,query) {
new TWTR.Widget({
  version: 2,
  type: 'search',
  search: query,
  interval: 6000,
  title: 'RUGoing',
  subject: eventTitle,
  width: 250,
  height: 300,
  theme: {
    shell: {
      background: '#000000',
      color: '#ff0011'
    },
    tweets: {
      background: '#ffffff',
      color: '#444444',
      links: '#1985b5'
    }
  },
  features: {
    scrollbar: false,
    loop: true,
    live: true,
    hashtags: true,
    timestamp: true,
    avatars: true,
    toptweets: true,
    behavior: 'default'
  }
}).render().start();
}
