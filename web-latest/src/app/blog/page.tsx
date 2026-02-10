import { Metadata } from "next";
import { BlogSection } from "@/components/sections/BlogSection";

export const metadata: Metadata = {
  title: "Elite Intelligence | TravelKing OMEGA Blog",
  description: "Global travel intelligence, legal mechanics, and sovereign logistics protocols.",
};

export default function BlogPage() {
  return (
    <main className="w-full bg-black min-h-screen pt-16">
      <BlogSection />
    </main>
  );
}
