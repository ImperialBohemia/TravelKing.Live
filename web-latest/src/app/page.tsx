"use client";

import { HeroSection } from "@/components/sections/HeroSection";
import { SearchSection } from "@/components/sections/SearchSection";
import { FeaturesSection } from "@/components/sections/FeaturesSection";
import { MapSection } from "@/components/sections/MapSection";
import { PricingSection } from "@/components/sections/PricingSection";
import { CTASection } from "@/components/sections/CTASection";

export default function Home() {
  return (
    <div className="flex flex-col w-full">
      <HeroSection />
      <SearchSection />
      <FeaturesSection />
      <MapSection />
      <PricingSection />
      <CTASection />
    </div>
  );
}
