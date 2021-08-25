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
  webpack(config) {
  config.module.rules.push({
    test: /\.svg$/,
    use: ["@svgr/webpack"]
  });

  return config;
}

}
