<script setup>
</script>

<template>
  <main class="bauhaus-canvas">
    
    <!-- Semantic Header for Screen Readers -->
    <h1 class="sr-only">Russ Hendy</h1>

    <!-- Background diagonal shapes (Infinite extension) -->
    <div class="bg-shape big-diagonal" aria-hidden="true"></div>

    <div class="content-wrapper">
        <!-- Main Rotated Group -->
        <div class="rotated-group">
            
            <!-- Creative Text Construction (Visual Only) -->
            <div class="text-composition" aria-hidden="true">
                <!-- "russ" -->
                <div class="row row-1">
                    <span class="letter">r</span>
                    <span class="letter">u</span>
                    <span class="letter">s</span>
                    <span class="letter">s</span>
                </div>
                
                <!-- "hendy" with extending lines -->
                <div class="row row-2">
                    <!-- The 'h' has a distinctive bar extending upwards -->
                    <div class="letter-container h-container">
                        <div class="extension-bar-up"></div>
                        <span class="letter">h</span>
                    </div>
                    
                    <div class="letter-container e-container">
                        <div class="e-bg-circle" aria-hidden="true"></div>
                        <div class="extension-bar-e-yellow" aria-hidden="true"></div>
                        <span class="letter">e</span>
                    </div>

                    <span class="letter">n</span>
                    <div class="letter-container d-container">
                        <span class="letter">d</span>
                        <div class="extension-bar-down" aria-hidden="true"></div>
                    </div>
                    <span class="letter">y</span>
                </div>
            </div>

            <!-- Geometric Accents attached to the rotation -->
            <div class="accent-circle" aria-hidden="true"></div>
            <div class="accent-line" aria-hidden="true"></div>
            <div class="accent-line accent-line-left" aria-hidden="true">
                <p>Contact: <a href="mailto:russhendy@gmail.com">Email</a> | <a href="https://www.linkedin.com/in/russ-hendy/">LinkedIn</a></p>
            </div>
            <div class="accent-block-top" aria-hidden="true"></div>
            
            <!-- Subtitle is readable text, keeping it visible but semantic -->
            <p class="subtitle subtitle-top">Digital & AI Consultant</p>
            <p class="subtitle"></p>
            <div class="rotated-again">
                <p class="body-copy">
                    I lead <strong>high performing teams</strong> to design and build <strong>exceptional digital services</strong>, including production <strong>AI-first products</strong>, for blue-chip clients.
                </p>
            </div>

            <div class="blue-block" aria-hidden="true"></div>
        </div>
    </div>

  </main>
</template>

<style scoped lang="scss">
@import '@/assets/styles/_mixins.scss';

.bauhaus-canvas {
    /* Component Variables */
    --bg-cream: #f4f4f0;
    --red: #d22630;
    --blue: #0063a6;
    --yellow: #fec300;
    --black: #1a1a1a;
    --orange: #f59e00;
    --title-spacing: -0.025em; /* Tweak this to adjust spacing */

    position: relative;
    width: 100vw;
    height: 100vh;
    background-color: var(--bg-cream);
    background-image: url('../assets/backgrounds/bauhaus-bg-coarse.png');
    background-repeat: repeat;
    overflow: hidden;
    font-family: 'Jost', sans-serif;
    color: var(--black);
}

/* Background elements that extend infinitely */
.bg-shape {
    position: absolute;
    z-index: 0;
}

.big-diagonal {
    width: 200vw;
    height: 400px;
    top: 50%;
    left: -50%;
    transform: rotate(-45deg) translateY(-50%);
}

.side-bar {
    position: absolute;
    top: 0;
    left: 10%;
    width: 40px;
    height: 100vh;
    background-color: rgba(0,0,0,0.03);
}

/* Centered Content Wrapper */
.content-wrapper {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10;
}

/* The Rotated Group (-45deg) */
.rotated-group {
    transform: rotate(-45deg);
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    position: relative;
}

.rotated-again {
    transform-origin: bottom left;
    position: relative;
}

/* Text Styling */
.text-composition {
    font-weight: 700;
    font-size: clamp(4rem, 10vw, 8rem);
    line-height: 0.9;
    letter-spacing: var(--title-spacing, -0.02em); /* Slightly open default */
    position: relative;
}

.row {
    display: flex;
    align-items: baseline;
}

.row-2 {
    margin-left: 1.5ch; /* Offset "hendy" slightly */
}

/* Letter Extensions (The "Bauhaus" look) */
.letter-container {
    position: relative;
    display: inline-flex;
    flex-direction: column;
    align-items: center;
}

/* The 'h' extension */
.extension-bar-up {
    position: absolute;
    top: 100%; /* Start from top of lowercase part roughly */
    left: 0.033em; /* Align with left stem */
    width: 0.15em; /* Match stroke width approx */

    height: 100vh; /* Extend infinitely upwards (relative to rotation) */
    background-color: var(--black);
    transform: translateX(15%); /* Fine tune alignment to font stem */
}

.extension-bar-e-yellow {
    position: absolute;
    top: 100%; /* Start from top of lowercase part roughly */
    left: 0.033em; /* Align with left stem */
    width: 0.8em; /* Match stroke width approx */
    opacity: 0.5;
    height: 100vh; /* Extend infinitely upwards (relative to rotation) */
    background-color: var(--yellow);
    transform: translate(-20%, 3%); /* Fine tune alignment to font stem */
}

/* The 'e' background circle */
.e-container {
    position: relative;
    /* No z-index on parent allows children to stack naturally in current context */
}

.e-bg-circle {
    position: absolute;
    top: 62.5%; /* Moved up from 55% */
    left: 55%; /* Moved left from 50% */
    transform: translate(-50%, -50%);
    width: 0.85em; 
    height: 0.85em;
    opacity: 0.65;
    background-color: #fec300; /* Hardcoded Bauhaus Yellow */
    mix-blend-mode: multiply; /* Better than opacity for visibility */
    border-radius: 50%;
    z-index: 0; 
}

.e-container .letter {
    position: relative;
    z-index: 1; 
}


/* The 'd' extension */
.extension-bar-down {
    position: absolute;
    bottom: 0.98em;
    right: 0.035em;
    width: 0.15em;
    height: 500vh;
    background-color: var(--orange);
    opacity: 0.8;
}

/* Accents */
.accent-circle {
    position: absolute;
    width: 15vw;
    height: 15vw;

    max-width: 12em;
    max-height: 12em;

    /* background-color: var(--red); REMOVED */
    background-image: url('../assets/russ-hendy.jpg');
    background-size: cover;
    background-position: center;
    border-radius: 50%;
    top: -6em;
    right: -5.5em; /* Adjusted to keep relative visual center: -5.5 + 6 = 0.5 offset */
    /* mix-blend-mode: multiply; REMOVED for photo visibility */
    z-index: -1;

    @include tablet {
        width: 25vw;
        height: 25vw;
        right: -8em;
    }
    
    @include mobile {
        width: 12em;
        height: 12em;
        right: -12em;
    }
}

.accent-line {
    position: absolute;
    height: 1.2rem;
    width: 200vw;
    background-color: var(--black);
    opacity: 0.3;
    top: 67%;
    left: -100vw;
    transform: translateY(1em);
    z-index: -2;
}


/* Left Accent Line */
.accent-line-left {
    position: absolute;
    width: 1.2rem;
    height: 200vh;
    background-color: var(--orange);
    top: -3.5%;
    left: -14%;
    z-index: -2;
    opacity: 0.8;

    p {
        transform-origin: top left;
        transform: rotate(90deg);
        font-size: 1.2rem;
        padding-top: .5rem;
        width: 500px;
    }
}


/* Red block */
.accent-block-top {
    position: absolute;
    height: 12em;
    width: 200vw;
    background-color: var(--red);
    top: -16.5em;
    right: 22.25%;
    transform: translateY(1em);
    z-index: -2;
}

.blue-block {
    position: absolute;
    width: 6em;
    height: 200vw;
    background-color: var(--blue);
    top: -70%;
    right: -38%;
    opacity: 0.8;
    transform: translateY(1em);
    z-index: 3;

    @include tablet {
        right: -50%;
    }

    @include mobile {
        right: -80%;
    }
}

.subtitle {
    font-size: 1.5rem;
    margin-bottom: 8em;
    line-height: 1.15em;
}

.subtitle-top {
    font-size: 2em;
    font-weight: 400;
    letter-spacing: 0em;
    margin-top: 0;
    margin-right: 0;
    margin-left: -14.5%;
    line-height: 1.15em;
    color: var(--black);
    position: absolute;
    top: -1.35em;
    min-width: 400px;
    font-size: 2em;

    @include tablet {
        font-size: 1.8em;
    }
    @include mobile {
        font-size: 1.6em;
    }
    
}


.body-copy {
    position: absolute;
    width: 330px;
    color: var(--black);
    font-weight: 300;
    font-size: 1rem;
    margin-top: -5em;
    left: 10.4em;

    @include tablet {
        left: 8em;
        margin-top: -4em;
    }
    @include mobile {
        left: -8.75em;
        margin-top: -2em;
        rotate: 90deg
    }
}

/* Screen Reader Only Utility (Backup) */
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
}

/* Mobile Adjustments */
</style>