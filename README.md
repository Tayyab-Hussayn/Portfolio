# Vue.js Portfolio Website

A complete and attractive portfolio website built with Vue.js, featuring responsive design, modern UI components, and smooth animations.

## 🚀 Features

### ✅ Navigation Bar
- Fixed top navbar with smooth scrolling
- Responsive design with mobile hamburger menu
- Active route highlighting
- Hover effects and transitions
- Links: Home, Projects, Contact Us, Hire a Developer, Login

### ✅ Hero Section
- Full-width banner with gradient background
- Animated background pattern
- Professional profile image placeholder
- Catchy headline: "Hi, I'm Alex Johnson, A Passionate Web Developer"
- Call-to-action buttons: "Hire Me" and "View Projects"
- Smooth animations and floating elements

### ✅ Services Section
- Grid layout with 4 service cards
- Services: Web Development, UI/UX Design, SEO Optimization, Freelancing
- Icons with color-coded themes
- Hover effects and animations
- Responsive design

### ✅ Projects Section
- Showcase of 6 featured projects
- Project cards with gradient backgrounds
- Tech stack tags
- "Live Preview" and "Code" buttons
- Category badges (Frontend, Full Stack)
- Responsive grid layout

### ✅ Contact Section
- Two-column layout (contact info + form)
- Contact form with validation
- Fields: Name, Email, Subject, Message
- Success message on submission
- Contact information with icons
- Social media links

### ✅ Login Component
- Modal-based login system
- Email and password fields with validation
- Remember me checkbox
- Forgot password link
- Social login options (Google, GitHub)
- Form validation and error handling

### ✅ Footer
- Multi-column layout
- Brand information and description
- Social media icons (GitHub, LinkedIn, Twitter, Dribbble, Instagram)
- Quick links and services
- Newsletter signup
- Copyright information
- "Back to top" button

### ✅ Additional Pages
- **Projects Page**: Dedicated page with filtering (All, Frontend, Full Stack, Mobile)
- **Contact Page**: Standalone contact page
- **Hire Page**: Detailed hiring information with pricing and process

### ✅ Technical Features
- Vue 3 with Composition API
- Vue Router for navigation
- Tailwind CSS for styling
- Responsive design (mobile-first)
- Smooth animations and transitions
- Modular component architecture
- Form validation
- Modern ES6+ JavaScript

## 🛠️ Technologies Used

- **Frontend Framework**: Vue.js 3
- **Routing**: Vue Router 4
- **Styling**: Tailwind CSS 3
- **Build Tool**: Vite
- **Icons**: Font Awesome
- **Fonts**: Inter (Google Fonts)

## 📁 Project Structure

```
portfolio-website/
├── public/
├── src/
│   ├── components/
│   │   ├── NavigationBar.vue
│   │   ├── HeroSection.vue
│   │   ├── ServicesSection.vue
│   │   ├── ServiceCard.vue
│   │   ├── ProjectsSection.vue
│   │   ├── ProjectCard.vue
│   │   ├── ContactSection.vue
│   │   ├── LoginModal.vue
│   │   └── FooterSection.vue
│   ├── views/
│   │   ├── Home.vue
│   │   ├── Projects.vue
│   │   ├── Contact.vue
│   │   └── Hire.vue
│   ├── router/
│   │   └── index.js
│   ├── assets/
│   ├── App.vue
│   ├── main.js
│   └── style.css
├── index.html
├── package.json
├── vite.config.js
├── tailwind.config.js
└── postcss.config.js
```

## 🚀 Getting Started

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Installation

1. **Clone or download the project**
   ```bash
   cd portfolio-website
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   Navigate to `http://localhost:3000`

### Build for Production

```bash
npm run build
```

The built files will be in the `dist/` directory.

### Preview Production Build

```bash
npm run preview
```

## 🎨 Customization

### Personal Information
Update the following files to customize with your information:

1. **Hero Section** (`src/components/HeroSection.vue`):
   - Change name from "Alex Johnson"
   - Update description and bio
   - Replace profile image

2. **Contact Information** (`src/components/ContactSection.vue`):
   - Update email, phone, and location
   - Change social media links

3. **Projects** (`src/components/ProjectsSection.vue` and `src/views/Projects.vue`):
   - Replace with your actual projects
   - Update project images, descriptions, and links

4. **Services** (`src/components/ServicesSection.vue`):
   - Modify services to match your offerings

### Styling
- Colors can be customized in `tailwind.config.js`
- Custom styles are in `src/style.css`
- Component-specific styles are in each `.vue` file

### Images
- Add your profile image to `src/assets/images/`
- Update project images
- Replace placeholder images with actual screenshots

## 📱 Responsive Design

The website is fully responsive and optimized for:
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (320px - 767px)

## 🔧 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to fork this project and customize it for your own portfolio!

## 📞 Support

If you have any questions or need help customizing the website, feel free to reach out!

---

**Built with ❤️ using Vue.js and Tailwind CSS**

