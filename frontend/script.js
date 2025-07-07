// Dark mode toggle
document.getElementById('toggleTheme').onclick = () => {
  document.body.classList.toggle('dark');
  const isDark = document.body.classList.contains('dark');
  document.getElementById('toggleTheme').textContent = isDark ? '☀️' : '🌙';
};



const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".popup-menu a, .nav-links a");

window.addEventListener("scroll", () => {
  let current = "";

  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.offsetHeight;
    if (scrollY >= sectionTop - sectionHeight / 3) {
      current = section.getAttribute("id");
    }
  });

  navLinks.forEach((link) => {
    link.classList.remove("active");
    if (link.getAttribute("href") === `#${current}`) {
      link.classList.add("active");
    }
  });
});


const menuToggle = document.getElementById("menuToggle");
const popupMenu = document.getElementById("popupMenu");

menuToggle.addEventListener("click", () => {
  popupMenu.classList.toggle("show");
});

// Optional: close when clicking outside
window.addEventListener("click", function (e) {
  if (!popupMenu.contains(e.target) && e.target !== menuToggle) {
    popupMenu.classList.remove("show");
  }
});




// Reveal on scroll
function revealOnScroll() {
  const elements = document.querySelectorAll('.reveal');
  const windowHeight = window.innerHeight;

  elements.forEach((el) => {
    const elementTop = el.getBoundingClientRect().top;
    if (elementTop < windowHeight - 100) {
      el.classList.add('active');
    }
  });
}

// Modal Logic
const modal = document.getElementById('projectModal');
const modalTitle = document.getElementById('modalTitle');
const modalImage = document.getElementById('modalImage');
const modalDesc = document.getElementById('modalDesc');
const modalTech = document.getElementById('modalTech');
const modalLink = document.getElementById('modalLink');
const closeBtn = document.querySelector('.close-btn');

document.querySelectorAll('.project-card').forEach(card => {
  card.addEventListener('click', () => {
    modalTitle.textContent = card.dataset.title;
    modalImage.src = card.dataset.image;
    modalDesc.textContent = card.dataset.desc;
    modalTech.textContent = card.dataset.tech;
    modalLink.href = card.dataset.link;

    modal.style.display = 'block';
  });
});

const contactForm = document.getElementById("contactForm");
const sendBtn = document.getElementById("sendBtn");

contactForm.addEventListener("submit", function (e) {
  e.preventDefault();
  sendBtn.classList.add("submitted");
  setTimeout(() => {
    sendBtn.classList.remove("submitted");
    contactForm.reset();
  }, 2000);
});


let lastScrollTop = 0;
const footer = document.querySelector(".fixed-footer");

window.addEventListener("scroll", () => {
  let currentScroll = window.pageYOffset || document.documentElement.scrollTop;
  if (currentScroll > lastScrollTop) {
    footer.classList.add("hidden"); // scrolling down
  } else {
    footer.classList.remove("hidden"); // scrolling up
  }
  lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
});


const form = document.getElementById("contactForm");

contactForm.addEventListener("submit", async function (e) {
  e.preventDefault();

  sendBtn.classList.add("submitted");

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const message = document.getElementById("message").value;

  try {
    const response = await fetch("https://api.iadiee.xyz/create_user", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email, message })
    });

    if (response.ok) {
      alert("Message sent!");
      contactForm.reset();
    } else {
      alert("Failed to send message.");
    }
  } catch (err) {
    alert("Network error.");
    console.error(err);
  }

  setTimeout(() => {
    sendBtn.classList.remove("submitted");
  }, 2000);
});




closeBtn.onclick = () => modal.style.display = 'none';
window.onclick = e => { if (e.target === modal) modal.style.display = 'none'; };


window.addEventListener('scroll', revealOnScroll);
window.addEventListener('load', revealOnScroll);


