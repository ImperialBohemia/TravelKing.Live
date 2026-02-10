import "@testing-library/jest-dom";
import { render, screen } from '@testing-library/react'
import { HeroSection } from '@/components/sections/HeroSection'

// Mock framer-motion
jest.mock('framer-motion', () => ({
  motion: {
    div: ({ children, ...props }: any) => <div {...props}>{children}</div>,
    h1: ({ children, ...props }: any) => <h1 {...props}>{children}</h1>,
    p: ({ children, ...props }: any) => <p {...props}>{children}</p>,
  },
}))

describe('HeroSection', () => {
  it('renders the Travel Supremacy headline', () => {
    render(<HeroSection />)
    const headline = screen.getByRole('heading', { name: /Travel/i })
    expect(headline).toBeInTheDocument()
  })
})
