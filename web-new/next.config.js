/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
  },
  async redirects() {
    return [
      {
        source: "/github",
        destination: "https://github.com/steven-tey/precedent",
        permanent: false,
      },
    ];
  },
};

module.exports = nextConfig;
