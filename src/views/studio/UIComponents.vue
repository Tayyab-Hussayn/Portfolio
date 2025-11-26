<template>
  <div class="min-h-screen pt-16 bg-gray-50/50">
    <!-- Hero Section -->
    <section class="bg-white border-b border-gray-100 relative overflow-hidden">
      <div class="container-custom py-20 md:py-32 text-center relative z-10">
        <div class="inline-flex items-center px-3 py-1 rounded-full bg-purple-50 text-purple-600 text-xs font-medium mb-6 border border-purple-100">
          <span class="flex h-2 w-2 rounded-full bg-purple-600 mr-2"></span>
          Studio Resources
        </div>
        
        <h1 class="text-4xl md:text-6xl font-bold text-gray-900 mb-6 tracking-tight leading-tight">
          Premium <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-pink-600">UI Components</span>
        </h1>
        
        <p class="text-xl text-gray-500 max-w-2xl mx-auto mb-12 leading-relaxed font-light">
          A collection of production-ready, beautifully designed components extracted from our premium projects. Copy, paste, and ship.
        </p>
      </div>
    </section>

    <!-- Components Grid -->
    <section class="container-custom py-16 md:py-24">
      <div class="grid grid-cols-1 gap-12">
        <ComponentCard 
          v-for="component in components" 
          :key="component.id" 
          :title="component.title"
          :description="component.description"
          :code="component.code"
        />
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ComponentCard from '@/components/studio/ComponentCard.vue'

defineOptions({
  name: 'UIComponents'
})

const components = ref([
  {
    id: 'hero',
    title: 'Modern SaaS Hero Section',
    description: 'A high-converting hero section with animated background shapes, glassmorphism effects, and a code window visual.',
    code: `<!-- Hero Section Component -->
<style>
    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

    /* CSS Custom Properties */
    :root {
        --tsp-primary: #453478;
        --tsp-primary-dark: #2d2152;
        --tsp-primary-light: #6a4bc4;
        --tsp-accent: #00d2ff;
        /* Cyan accent for digital feel */
        --tsp-text-light: #ffffff;
        --tsp-text-dim: #e0e0e0;
        --tsp-glass-bg: rgba(255, 255, 255, 0.05);
        --tsp-glass-border: rgba(255, 255, 255, 0.1);
    }

    /* Hero Section Base */
    .tsp-hero {
        position: relative;
        min-height: 100vh;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        background: radial-gradient(circle at top left, #1a1a2e 0%, #0f0f12 100%);
        padding: 200px 40px 120px 30px;
        box-sizing: border-box;
        font-family: 'Inter', sans-serif;
    }

    /* Animated Background Elements */
    .tsp-bg-shape {
        position: absolute;
        border-radius: 50%;
        filter: blur(80px);
        opacity: 0.4;
        z-index: 0;
        animation: float 10s infinite ease-in-out;
    }

    .tsp-shape-1 {
        top: -10%;
        left: -10%;
        width: 600px;
        height: 600px;
        background: var(--tsp-primary);
        animation-delay: 0s;
    }

    .tsp-shape-2 {
        bottom: -10%;
        right: -5%;
        width: 500px;
        height: 500px;
        background: var(--tsp-primary-light);
        animation-delay: -5s;
    }

    .tsp-shape-3 {
        top: 40%;
        left: 50%;
        width: 300px;
        height: 300px;
        background: var(--tsp-accent);
        opacity: 0.15;
        animation-delay: -2s;
    }

    @keyframes float {

        0%,
        100% {
            transform: translate(0, 0);
        }

        50% {
            transform: translate(30px, -30px);
        }
    }

    /* Container */
    .tsp-container {
        max-width: 1280px;
        width: 100%;
        margin: 0 auto;
        position: relative;
        z-index: 1;
        display: grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 60px;
        align-items: center;
    }

    /* Content Side */
    .tsp-hero-content {
        display: flex;
        flex-direction: column;
        gap: 32px;
    }

    .tsp-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 16px;
        background: rgba(69, 52, 120, 0.3);
        border: 1px solid var(--tsp-primary-light);
        border-radius: 100px;
        width: fit-content;
        backdrop-filter: blur(10px);
    }

    .tsp-badge-dot {
        width: 8px;
        height: 8px;
        background-color: var(--tsp-accent);
        border-radius: 50%;
        box-shadow: 0 0 10px var(--tsp-accent);
    }

    .tsp-badge-text {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        font-weight: 500;
        color: var(--tsp-text-light);
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }

    .tsp-headline {
        font-family: 'Outfit', sans-serif;
        font-size: 64px;
        font-weight: 800;
        line-height: 1.1;
        color: var(--tsp-text-light);
        margin: 0;
        letter-spacing: -1px;
    }

    .tsp-headline-highlight {
        background: linear-gradient(135deg, #fff 0%, #a5a5a5 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        display: block;
    }

    .tsp-headline-gradient {
        background: linear-gradient(90deg, var(--tsp-accent) 0%, var(--tsp-primary-light) 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .tsp-subheading {
        font-size: 18px;
        line-height: 1.6;
        color: var(--tsp-text-dim);
        max-width: 600px;
        margin: 0;
    }

    /* Buttons */
    .tsp-cta-group {
        display: flex;
        gap: 20px;
        margin-top: 16px;
    }

    .tsp-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 16px 32px;
        font-family: 'Outfit', sans-serif;
        font-size: 16px;
        font-weight: 600;
        border-radius: 12px;
        text-decoration: none;
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .tsp-btn-primary {
        background: linear-gradient(135deg, var(--tsp-primary) 0%, var(--tsp-primary-light) 100%);
        color: white;
        border: none;
        box-shadow: 0 10px 20px rgba(69, 52, 120, 0.3);
    }

    .tsp-btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 30px rgba(69, 52, 120, 0.4);
    }

    .tsp-btn-secondary {
        background: rgba(255, 255, 255, 0.05);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }

    .tsp-btn-secondary:hover {
        background: rgba(255, 255, 255, 0.1);
        border-color: rgba(255, 255, 255, 0.3);
    }

    /* Visual Side (Code Window) */
    .tsp-hero-visual {
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        perspective: 1000px;
    }

    .tsp-code-window {
        width: 100%;
        background: #0d0d12;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.05);
        overflow: hidden;
        animation: floatCard 8s infinite ease-in-out;
        display: flex;
        flex-direction: column;
    }

    .tsp-window-header {
        background: #1a1a23;
        padding: 12px 16px;
        display: flex;
        align-items: center;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        position: relative;
    }

    .tsp-window-controls {
        display: flex;
        gap: 8px;
    }

    .tsp-control {
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }

    .tsp-close {
        background: #ff5f56;
    }

    .tsp-minimize {
        background: #ffbd2e;
    }

    .tsp-maximize {
        background: #27c93f;
    }

    .tsp-window-title {
        position: absolute;
        left: 0;
        right: 0;
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: rgba(255, 255, 255, 0.4);
        pointer-events: none;
    }

    .tsp-window-body {
        display: flex;
        min-height: 320px;
    }

    /* Code Section */
    .tsp-code-section {
        flex: 1.4;
        background: #0d0d12;
        padding: 20px;
        display: flex;
        gap: 16px;
        font-family: 'Fira Code', monospace;
        /* Fallback to monospace if not loaded */
        font-size: 13px;
        line-height: 1.6;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }

    .tsp-line-numbers {
        display: flex;
        flex-direction: column;
        color: rgba(255, 255, 255, 0.2);
        user-select: none;
        text-align: right;
    }

    .tsp-code-content {
        margin: 0;
        color: #a9b7c6;
    }

    /* Syntax Highlighting */
    .tsp-k {
        color: #cc7832;
    }

    /* Keyword (orange) */
    .tsp-v {
        color: #a9b7c6;
    }

    /* Variable (white/grey) */
    .tsp-f {
        color: #ffc66d;
    }

    /* Function (yellow) */
    .tsp-s {
        color: #6a8759;
    }

    /* String (green) */
    .tsp-c {
        color: #808080;
        font-style: italic;
    }

    /* Comment (grey) */
    .tsp-p {
        color: #9876aa;
    }

    /* Property (purple) */

    .tsp-cursor {
        display: inline-block;
        width: 2px;
        height: 1.2em;
        background: var(--tsp-accent);
        vertical-align: text-bottom;
        animation: blink 1s step-end infinite;
    }

    @keyframes blink {
        50% {
            opacity: 0;
        }
    }

    /* Preview Section */
    .tsp-preview-section {
        flex: 1;
        background: linear-gradient(135deg, #13131a 0%, #0f0f12 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
        position: relative;
        overflow: hidden;
    }

    .tsp-preview-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at center, rgba(69, 52, 120, 0.2) 0%, transparent 70%);
    }

    .tsp-preview-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 20px;
        width: 140px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        position: relative;
        z-index: 1;
    }

    .tsp-card-icon {
        width: 40px;
        height: 40px;
        background: rgba(0, 210, 255, 0.1);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--tsp-accent);
    }

    .tsp-card-stat {
        font-size: 24px;
        font-weight: 700;
        color: white;
    }

    .tsp-card-label {
        font-size: 12px;
        color: rgba(255, 255, 255, 0.5);
    }

    .tsp-card-graph {
        display: flex;
        gap: 4px;
        align-items: flex-end;
        height: 30px;
        margin-top: 5px;
    }

    .tsp-graph-bar {
        width: 6px;
        background: var(--tsp-primary-light);
        border-radius: 2px;
    }

    .tsp-graph-bar:last-child {
        background: var(--tsp-accent);
    }

    /* Floating Elements */
    .tsp-float-icon {
        position: absolute;
        width: 50px;
        height: 50px;
        background: rgba(30, 30, 40, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
        z-index: 2;
        animation: float 6s infinite ease-in-out;
    }

    @keyframes floatCard {

        0%,
        100% {
            transform: translateY(0);
        }

        50% {
            transform: translateY(-15px);
        }
    }

    /* Responsive */
    @media (max-width: 1024px) {
        .tsp-headline {
            font-size: 48px;
        }

        .tsp-container {
            gap: 40px;
        }
    }

    @media (max-width: 900px) {
        .tsp-container {
            grid-template-columns: 1fr;
            text-align: center;
        }

        .tsp-hero-content {
            align-items: center;
        }

        .tsp-subheading {
            margin: 0 auto;
        }

        .tsp-cta-group {
            justify-content: center;
        }

        .tsp-hero-visual {
            margin-top: 40px;
            width: 80%;
            margin-left: auto;
            margin-right: auto;
        }
    }

    @media (max-width: 480px) {
        .tsp-headline {
            font-size: 36px;
        }

        .tsp-hero {
            padding: 80px 20px;
        }

        .tsp-cta-group {
            flex-direction: column;
            width: 100%;
        }

        .tsp-btn {
            width: 100%;
            box-sizing: border-box;
        }

        .tsp-hero-visual {
            width: 100%;
        }

        .tsp-window-body {
            flex-direction: column;
        }

        .tsp-code-section {
            border-right: none;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }
    }
</style>

<section class="tsp-hero">
    <!-- Background Shapes -->
    <div class="tsp-bg-shape tsp-shape-1"></div>
    <div class="tsp-bg-shape tsp-shape-2"></div>
    <div class="tsp-bg-shape tsp-shape-3"></div>

    <div class="tsp-container">
        <!-- Left Content -->
        <div class="tsp-hero-content">
            <div class="tsp-badge">
                <span class="tsp-badge-dot"></span>
                <span class="tsp-badge-text">#1 Digital Agency</span>
            </div>

            <h1 class="tsp-headline">
                <span class="tsp-headline-highlight">Transforming Ideas into</span>
                <span class="tsp-headline-gradient">Digital Reality</span>
            </h1>

            <p class="tsp-subheading">
                We are a full-cycle software and digital agency helping businesses scale with cutting-edge
                technology, stunning design, and robust engineering.
            </p>

            <div class="tsp-cta-group">
                <a href="#" class="tsp-btn tsp-btn-primary">Start Your Project</a>
                <a href="#" class="tsp-btn tsp-btn-secondary">View Portfolio</a>
            </div>
        </div>

        <!-- Right Visual -->
        <div class="tsp-hero-visual">
            <!-- Code Window -->
            <div class="tsp-code-window">
                <div class="tsp-window-header">
                    <div class="tsp-window-controls">
                        <span class="tsp-control tsp-close"></span>
                        <span class="tsp-control tsp-minimize"></span>
                        <span class="tsp-control tsp-maximize"></span>
                    </div>
                    <div class="tsp-window-title">Techspirex Engine</div>
                </div>
                <div class="tsp-window-body">
                    <!-- Code Editor Side -->
                    <div class="tsp-code-section">
                        <div class="tsp-line-numbers">
                            <span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span><span>10</span>
                        </div>
                        <pre class="tsp-code-content"><code><span class="tsp-k">import</span> { <span class="tsp-v">DigitalTransformation</span> } <span class="tsp-k">from</span> <span class="tsp-s">'@techspirex/core'</span>;

<span class="tsp-c">// Initialize Project</span>
<span class="tsp-k">const</span> <span class="tsp-v">project</span> = <span class="tsp-k">new</span> <span class="tsp-f">DigitalTransformation</span>({
  <span class="tsp-p">client</span>: <span class="tsp-s">'Visionary Brand'</span>,
  <span class="tsp-p">goals</span>: [<span class="tsp-s">'Scale'</span>, <span class="tsp-s">'Innovate'</span>],
  <span class="tsp-p">techStack</span>: [<span class="tsp-s">'AI'</span>, <span class="tsp-s">'Cloud'</span>, <span class="tsp-s">'Web3'</span>]
});

<span class="tsp-k">await</span> <span class="tsp-v">project</span>.<span class="tsp-f">launch</span>();
<span class="tsp-c">// Status: 🚀 Deployed</span></code><span class="tsp-cursor">|</span></pre>
                    </div>

                    <!-- Preview Side -->
                    <div class="tsp-preview-section">
                        <div class="tsp-preview-card">
                            <div class="tsp-card-icon">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="2">
                                    <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
                                </svg>
                            </div>
                            <div class="tsp-card-stat">98%</div>
                            <div class="tsp-card-label">Performance</div>
                            <div class="tsp-card-graph">
                                <div class="tsp-graph-bar" style="height: 40%"></div>
                                <div class="tsp-graph-bar" style="height: 70%"></div>
                                <div class="tsp-graph-bar" style="height: 50%"></div>
                                <div class="tsp-graph-bar" style="height: 100%"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Floating Elements (Kept for depth) -->
            <div class="tsp-float-icon tsp-float-1" style="top: -30px; right: -30px;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00d2ff" stroke-width="2"
                    stroke-linecap="round" stroke-linejoin="round">
                    <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
                    <polyline points="2 17 12 22 22 17"></polyline>
                    <polyline points="2 12 12 17 22 12"></polyline>
                </svg>
            </div>
        </div>
    </div>
</section>`
  },
  {
    id: 'services',
    title: 'Premium Services Bento Grid',
    description: 'A modern bento-grid style services section with hover effects, glassmorphism, and responsive layout.',
    code: `<!-- Techspirex Premium Services Ecosystem -->
<style>
  /* Google Fonts */
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

  /* Scoped Variables & Styles */
  .tsp-services-section {
    --tsp-dark-bg: #0f0f12;
    --tsp-card-bg: rgba(255, 255, 255, 0.03);
    --tsp-card-border: rgba(255, 255, 255, 0.08);
    --tsp-primary: #453478;
    --tsp-accent: #00d2ff;
    --tsp-accent-glow: rgba(0, 210, 255, 0.3);
    --tsp-text-main: #ffffff;
    --tsp-text-muted: #a0a0a0;

    /* Reset & Base Styles for this section only */
    font-family: 'Inter', sans-serif;
    background-color: var(--tsp-dark-bg);
    position: relative;
    padding: 120px 20px;
    background: radial-gradient(circle at 50% 0%, #1a1a2e 0%, #0f0f12 60%);
    overflow: hidden;
    /* Ensure it takes full width but doesn't force height on parent if not needed, 
           though min-height is good for hero-like sections */
    width: 100%;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    box-sizing: border-box;
  }

  /* Background Ambient Glow */
  .tsp-ambient-glow {
    position: absolute;
    width: 800px;
    height: 800px;
    background: radial-gradient(circle, rgba(69, 52, 120, 0.15) 0%, transparent 70%);
    top: -200px;
    left: 50%;
    transform: translateX(-50%);
    pointer-events: none;
    z-index: 0;
  }

  /* Header */
  .tsp-section-header {
    position: relative;
    z-index: 2;
    text-align: center;
    max-width: 800px;
    margin-bottom: 80px;
  }

  .tsp-label {
    display: inline-block;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--tsp-accent);
    margin-bottom: 16px;
    padding: 6px 16px;
    background: rgba(0, 210, 255, 0.1);
    border-radius: 100px;
    border: 1px solid rgba(0, 210, 255, 0.2);
  }

  .tsp-title {
    font-family: 'Outfit', sans-serif;
    font-size: 56px;
    font-weight: 800;
    line-height: 1.1;
    color: var(--tsp-text-main);
    margin: 0 0 24px 0;
  }

  .tsp-title-gradient {
    background: linear-gradient(135deg, #fff 0%, #a5a5a5 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .tsp-subtitle {
    font-size: 18px;
    color: var(--tsp-text-muted);
    line-height: 1.6;
    max-width: 600px;
    margin: 0 auto;
  }

  /* Bento Grid */
  .tsp-bento-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(2, minmax(320px, auto));
    gap: 24px;
    max-width: 1400px;
    width: 100%;
    position: relative;
    z-index: 2;
  }

  /* Card Styles */
  .tsp-card {
    position: relative;
    background: var(--tsp-card-bg);
    border: 1px solid var(--tsp-card-border);
    border-radius: 24px;
    padding: 40px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
    backdrop-filter: blur(20px);
  }

  .tsp-card:hover {
    transform: translateY(-8px);
    border-color: rgba(255, 255, 255, 0.2);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    background: rgba(255, 255, 255, 0.05);
  }

  /* Grid Spans */
  .tsp-span-2 {
    grid-column: span 2;
  }

  .tsp-span-1 {
    grid-column: span 1;
  }

  /* Card Content */
  .tsp-card-header {
    position: relative;
    z-index: 2;
  }

  .tsp-card-icon {
    width: 64px;
    height: 64px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 24px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.4s ease;
  }

  .tsp-card:hover .tsp-card-icon {
    background: var(--tsp-primary);
    border-color: var(--tsp-primary-light);
    transform: scale(1.1) rotate(5deg);
  }

  .tsp-card-icon img {
    width: 36px;
    height: 36px;
    object-fit: contain;
    filter: brightness(0) invert(1);
  }

  .tsp-card-title {
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    font-weight: 700;
    color: var(--tsp-text-main);
    margin: 0 0 12px 0;
  }

  .tsp-card-desc {
    font-size: 15px;
    color: var(--tsp-text-muted);
    line-height: 1.6;
    margin: 0;
  }

  /* Card Footer / Action */
  .tsp-card-footer {
    margin-top: 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    z-index: 2;
  }

  .tsp-learn-more {
    color: var(--tsp-text-main);
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
    opacity: 0.7;
    transition: all 0.3s ease;
  }

  .tsp-card:hover .tsp-learn-more {
    opacity: 1;
    gap: 12px;
    color: var(--tsp-accent);
  }

  /* Visual Decorations */
  .tsp-card-bg-visual {
    position: absolute;
    bottom: -50px;
    right: -50px;
    width: 200px;
    height: 200px;
    background: radial-gradient(circle, var(--tsp-primary) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.5s ease;
    filter: blur(60px);
    pointer-events: none;
  }

  .tsp-card:hover .tsp-card-bg-visual {
    opacity: 0.4;
  }

  /* Specific Card Tweaks */
  .tsp-card-featured {
    background: linear-gradient(135deg, rgba(69, 52, 120, 0.2) 0%, rgba(255, 255, 255, 0.03) 100%);
  }

  /* Responsive */
  @media (max-width: 1200px) {
    .tsp-bento-grid {
      grid-template-columns: repeat(3, 1fr);
    }

    .tsp-span-2 {
      grid-column: span 2;
    }
  }

  @media (max-width: 900px) {
    .tsp-bento-grid {
      grid-template-columns: repeat(2, 1fr);
    }

    .tsp-span-2 {
      grid-column: span 2;
    }

    .tsp-title {
      font-size: 42px;
    }
  }

  @media (max-width: 600px) {
    .tsp-bento-grid {
      display: flex;
      flex-direction: column;
    }

    .tsp-card {
      min-height: auto;
    }

    .tsp-title {
      font-size: 32px;
    }

    .tsp-services-section {
      padding: 80px 20px;
    }
  }
</style>

<section class="tsp-services-section">
  <div class="tsp-ambient-glow"></div>

  <div class="tsp-section-header">
    <span class="tsp-label">Our Expertise</span>
    <h2 class="tsp-title">
      <span class="tsp-title-gradient">Engineering the Future</span><br>
      of Digital Business
    </h2>
    <p class="tsp-subtitle">
      We don't just build software; we craft digital ecosystems. From core infrastructure to customer experience,
      we deliver excellence at every layer.
    </p>
  </div>

  <div class="tsp-bento-grid">
    <!-- 1. Web & App (Featured, Span 2) -->
    <div class="tsp-card tsp-span-2 tsp-card-featured">
      <div class="tsp-card-bg-visual"></div>
      <div class="tsp-card-header">
        <div class="tsp-card-icon">
          <img src="https://cdn-icons-png.flaticon.com/512/2010/2010990.png" alt="Web & App Development">
        </div>
        <h3 class="tsp-card-title">Web & App Development</h3>
        <p class="tsp-card-desc">
          Scalable, high-performance architectures built for the modern web. We engineer robust applications
          that drive business growth and user engagement.
        </p>
      </div>
      <div class="tsp-card-footer">
        <a href="https://techspirex.com/service/web-app-development/" class="tsp-learn-more">Explore Solutions
          <span style="font-size: 18px;">→</span></a>
      </div>
    </div>

    <!-- 2. Design (Span 1) -->
    <div class="tsp-card tsp-span-1">
      <div class="tsp-card-bg-visual"></div>
      <div class="tsp-card-header">
        <div class="tsp-card-icon">
          <img
            src="https://img.icons8.com/external-kmg-design-flat-kmg-design/64/external-pen-tool-graphic-design-kmg-design-flat-kmg-design.png"
            alt="UI/UX Design">
        </div>
        <h3 class="tsp-card-title">UI/UX Design</h3>
        <p class="tsp-card-desc">
          Award-winning aesthetics meet intuitive functionality. We design interfaces that users love.
        </p>
      </div>
      <div class="tsp-card-footer">
        <a href="https://techspirex.com/service/graphic-ui-ux-design" class="tsp-learn-more">View Designs <span
            style="font-size: 18px;">→</span></a>
      </div>
    </div>

    <!-- 3. Digital Marketing (Span 1) -->
    <div class="tsp-card tsp-span-1">
      <div class="tsp-card-bg-visual"></div>
      <div class="tsp-card-header">
        <div class="tsp-card-icon">
          <img src="https://cdn-icons-png.flaticon.com/512/8292/8292355.png" alt="Digital Marketing">
        </div>
        <h3 class="tsp-card-title">Digital Marketing</h3>
        <p class="tsp-card-desc">
          Data-driven strategies to amplify your brand presence and maximize ROI across all channels.
        </p>
      </div>
      <div class="tsp-card-footer">
        <a href="https://techspirex.com/service/digital-marketing/" class="tsp-learn-more">Grow Traffic <span
            style="font-size: 18px;">→</span></a>
      </div>
    </div>

    <!-- 4. E-commerce (Span 1) -->
    <div class="tsp-card tsp-span-1">
      <div class="tsp-card-bg-visual"></div>
      <div class="tsp-card-header">
        <div class="tsp-card-icon">
          <img src="https://cdn-icons-png.flaticon.com/512/9674/9674658.png" alt="E-commerce">
        </div>
        <h3 class="tsp-card-title">E-commerce</h3>
        <p class="tsp-card-desc">
          Seamless shopping experiences with secure payment integration and conversion optimization.
        </p>
      </div>
      <div class="tsp-card-footer">
        <a href="https://techspirex.com/service/e-commerce-solutions" class="tsp-learn-more">Sell Online <span
            style="font-size: 18px;">→</span></a>
      </div>
    </div>

    <!-- 5. DevOps (Featured, Span 2) -->
    <div class="tsp-card tsp-span-2 tsp-card-featured">
      <div class="tsp-card-bg-visual"></div>
      <div class="tsp-card-header">
        <div class="tsp-card-icon">
          <img src="https://cdn-icons-png.flaticon.com/512/5266/5266248.png" alt="DevOps & Cloud Infrastructure">
        </div>
        <h3 class="tsp-card-title">DevOps & Cloud Infrastructure</h3>
        <p class="tsp-card-desc">
          Automate your pipeline and scale with confidence. We implement robust CI/CD workflows and
          cloud-native architectures for maximum efficiency and uptime.
        </p>
      </div>
      <div class="tsp-card-footer">
        <a href="https://techspirex.com/service/devops-cloud" class="tsp-learn-more">Optimize Ops <span
            style="font-size: 18px;">→</span></a>
      </div>
    </div>

    <!-- 6. SEO (Span 1) -->
    <div class="tsp-card tsp-span-1">
      <div class="tsp-card-bg-visual"></div>
      <div class="tsp-card-header">
        <div class="tsp-card-icon">
          <img src="https://cdn-icons-png.flaticon.com/512/10302/10302417.png" alt="SEO Optimization">
        </div>
        <h3 class="tsp-card-title">SEO Optimization</h3>
        <p class="tsp-card-desc">
          Dominate search rankings with comprehensive, data-backed SEO strategies.
        </p>
      </div>
      <div class="tsp-card-footer">
        <a href="https://techspirex.com/service/seo/" class="tsp-learn-more">Rank Higher <span
            style="font-size: 18px;">→</span></a>
      </div>
    </div>
  </div>
</section>`
  }
])
</script>
