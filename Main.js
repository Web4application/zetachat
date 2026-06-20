import { DiscordSDK } from "@discord/embedded-app-sdk";

const discordSdk = new DiscordSDK(
  import.meta.env.VITE_DISCORD_CLIENT_ID
);

// ---------------------
// APP UI
// ---------------------

document.querySelector("#app").innerHTML = `
<div class="web4-container">

  <canvas id="matrix-canvas"></canvas>
  <canvas id="stars-canvas"></canvas>

  <div class="avatar-panel">
      <canvas id="avatar-canvas"></canvas>
      <div id="link-status">OFFLINE</div>
  </div>

  <div class="glass-container">

      <div class="chat-window" id="chat">
          <div class="message system">
              WEB4 CORE INITIALIZED
          </div>
      </div>

      <div class="input-area">
          <input id="msgInput" placeholder="Transmit Data..." />
          <button id="sendBtn">SEND</button>
      </div>

  </div>

</div>
`;

// ---------------------
// DISCORD INIT
// ---------------------

(async () => {
    try {
        await discordSdk.ready();
        addMessage("Discord Activity Connected");
    } catch {
        addMessage("Discord Activity Offline");
    }
})();

// ---------------------
// CHAT
// ---------------------

function addMessage(text, user = false) {

    const chat = document.getElementById("chat");

    const div = document.createElement("div");

    div.className = `message ${user ? "user" : "system"}`;

    chat.appendChild(div);

    decodeMessage(div, text);

    chat.scrollTop = chat.scrollHeight;
}

document
.getElementById("sendBtn")
.addEventListener("click", sendMessage);

async function sendMessage() {

    const input = document.getElementById("msgInput");

    if (!input.value.trim()) return;

    addMessage(input.value, true);

    const prompt = input.value;

    input.value = "";

    setTimeout(() => {
        addMessage(
            `WEB4 AI: Processing "${prompt}"`,
            false
        );
    }, 600);
}

// ---------------------
// CANVAS
// ---------------------

const matrixCanvas =
document.getElementById("matrix-canvas");

const starCanvas =
document.getElementById("stars-canvas");

const avatarCanvas =
document.getElementById("avatar-canvas");

const mCtx = matrixCanvas.getContext("2d");
const sCtx = starCanvas.getContext("2d");
const aCtx = avatarCanvas.getContext("2d");

let width;
let height;
let drops = [];

function resize() {

    width = window.innerWidth;
    height = window.innerHeight;

    matrixCanvas.width = width;
    matrixCanvas.height = height;

    starCanvas.width = width;
    starCanvas.height = height;

    avatarCanvas.width = 250;
    avatarCanvas.height = 250;

    drops = Array(
        Math.floor(width / 20)
    ).fill(1);
}

window.addEventListener(
    "resize",
    resize
);

resize();

// ---------------------
// MATRIX RAIN
// ---------------------

const matrixChars =
"01ΣΔΩΨWEB4AI";

function renderMatrix() {

    mCtx.fillStyle =
        "rgba(0,0,0,0.05)";

    mCtx.fillRect(
        0,
        0,
        width,
        height
    );

    mCtx.fillStyle = "#00f2ff";

    drops.forEach((y, i) => {

        const char =
            matrixChars[
                Math.floor(
                    Math.random() *
                    matrixChars.length
                )
            ];

        mCtx.fillText(
            char,
            i * 20,
            y * 20
        );

        if (
            y * 20 > height &&
            Math.random() > 0.975
        ) {
            drops[i] = 0;
        }

        drops[i]++;
    });
}

// ---------------------
// STARFIELD
// ---------------------

const stars = Array.from(
    { length: 150 },
    () => ({
        x: Math.random() * width,
        y: Math.random() * height,
        size: Math.random() * 2
    })
);

function renderStars() {

    sCtx.clearRect(
        0,
        0,
        width,
        height
    );

    stars.forEach(star => {

        sCtx.beginPath();

        sCtx.arc(
            star.x,
            star.y,
            star.size,
            0,
            Math.PI * 2
        );

        sCtx.fillStyle = "#fff";
        sCtx.fill();

        star.y -= 0.4;

        if (star.y < 0) {
            star.y = height;
        }
    });
}

// ---------------------
// AUDIO
// ---------------------

const audioCtx =
new (
    window.AudioContext ||
    window.webkitAudioContext
)();

let analyser;
let dataArray;

async function startVoice() {

    const stream =
        await navigator
        .mediaDevices
        .getUserMedia({
            audio: true
        });

    const source =
        audioCtx
        .createMediaStreamSource(
            stream
        );

    analyser =
        audioCtx.createAnalyser();

    source.connect(analyser);

    analyser.fftSize = 64;

    dataArray =
        new Uint8Array(
            analyser.frequencyBinCount
        );

    document.getElementById(
        "link-status"
    ).innerText = "ONLINE";
}

window.addEventListener(
    "click",
    async () => {

        await audioCtx.resume();

        if (!analyser) {
            await startVoice();
        }
    },
    { once: true }
);

// ---------------------
// AVATAR
// ---------------------

function renderAvatar() {

    if (!analyser) return;

    analyser.getByteFrequencyData(
        dataArray
    );

    const volume =
        dataArray.reduce(
            (a, b) => a + b,
            0
        ) / dataArray.length;

    const radius =
        50 + volume / 3;

    aCtx.clearRect(
        0,
        0,
        250,
        250
    );

    aCtx.beginPath();

    aCtx.arc(
        125,
        125,
        radius,
        0,
        Math.PI * 2
    );

    aCtx.strokeStyle =
        volume > 50
            ? "#bc13fe"
            : "#00f2ff";

    aCtx.lineWidth = 3;

    aCtx.stroke();
}

// ---------------------
// GLITCH TEXT
// ---------------------

const scrambleChars =
"!<>-_\\/[]{}=*?#";

function decodeMessage(
    element,
    finalText
) {

    let iteration = 0;

    const interval =
    setInterval(() => {

        element.textContent =
        finalText
            .split("")
            .map((char, index) => {

                if (
                    index < iteration
                ) {
                    return finalText[index];
                }

                return scrambleChars[
                    Math.floor(
                        Math.random() *
                        scrambleChars.length
                    )
                ];
            })
            .join("");

        if (
            iteration >=
            finalText.length
        ) {
            clearInterval(
                interval
            );
        }

        iteration += 0.4;

    }, 30);
}

// ---------------------
// MAIN LOOP
// ---------------------

function animate() {

    renderMatrix();
    renderStars();
    renderAvatar();

    requestAnimationFrame(
        animate
    );
}

animate();
