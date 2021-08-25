module.exports = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: '/api',
        destination: 'http://localhost:5000/',
      },
    ]
  },
}
