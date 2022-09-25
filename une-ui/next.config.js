/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: [
      'www.lac.inpe.br',
      'sophiaweb.mctic.gov.br',
      'images-na.ssl-images-amazon.com', 'localhost']
  }
}

module.exports = nextConfig
