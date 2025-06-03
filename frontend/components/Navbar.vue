<template>
  <nav class="navbar ">
    <!-- Desktop Navigation -->
    <div class="desktop-nav">
      <div class="nav-brand">
        <!-- <img
          class="logo"
          src="https://img.icons8.com/pulsar-color/48/twitterx.png"
          alt="X-Tweet logo"
        /> -->
        <h1 class="title">{{ title }}</h1>
      </div>

      <ul class="nav-items ">
        <li v-for="(item, index) in links" :key="index" class="nav-item">
          <div v-if="!item.children" class="nav-link-wrapper">
            <NuxtLink
              :to="item.path"
              class="nav-link"
              :class="{ 'active-link': activeIndex === index }"
              @click.native="setActive(index)"
            >
              {{ item.name }}
            </NuxtLink>
          </div>

          <!-- Dropdown Parent -->
          <div
            v-else
            class="dropdown-parent"
            @mouseenter="dropdownOpenIndex = index"
            @mouseleave="dropdownOpenIndex = null"
          >
            <div
              class="nav-link"
              :class="{
                'active-link': activeIndex === index,
                'dropdown-open': dropdownOpenIndex === index,
              }"
              @click="toggleDropdown(index)"
            >
              {{ item.name }}
              <span class="dropdown-arrow">▼</span>
            </div>

            <!-- Dropdown Content -->
            <transition name="dropdown">
              <ul v-if="dropdownOpenIndex === index" class="dropdown-menu">
                <li
                  v-for="(child, childIndex) in item.children"
                  :key="childIndex"
                  class="dropdown-item"
                  @click="setActiveChild(index, childIndex)"
                >
                  <NuxtLink
                    :to="child.path"
                    class="dropdown-link"
                    :class="{
                      'active-link':
                        activeChildIndex === childIndex &&
                        activeIndex === index,
                    }"
                  >
                    {{ child.name }}
                  </NuxtLink>
                </li>
              </ul>
            </transition>
          </div>
        </li>
      </ul>

      <!-- Auth Section -->
      <!-- <div class="auth-links">
        <div v-if="!isLoggedIn" class="login-button" @click="login">Login</div>

        <div
          v-else
          class="profile-dropdown"
          @mouseenter="isProfileDropdownOpen = true"
          @mouseleave="isProfileDropdownOpen = false"
        >
          <div class="profile-info">
            <img
              :src="userProfile.avatar"
              class="profile-avatar"
              alt="Profile"
            />
            <span class="profile-name">{{ userProfile.name }}</span>
          </div>

          <transition name="dropdown">
            <ul v-if="isProfileDropdownOpen" class="dropdown-menu profile-menu">
              <li class="dropdown-item">
                <div class="dropdown-link" @click="viewProfile">
                  <span>👤</span> Profile
                </div>
              </li>
              <li class="dropdown-item">
                <div class="dropdown-link" @click="logout">
                  <span>🚪</span> Logout
                </div>
              </li>
            </ul>
          </transition>
        </div>
      </div> -->
    </div>

    <!-- Mobile Navigation -->
    <div class="mobile-nav">
      <div class="nav-brand">
        <img
          width="36"
          height="36"
          src="https://img.icons8.com/pulsar-color/48/twitterx.png"
          alt="X-Tweet logo"
        />
        <h1 class="title">{{ title }}</h1>
      </div>
      <button class="menu-toggle" @click="toggleMobileMenu">☰</button>
    </div>

    <!-- Mobile Dropdown Menu -->
    <transition name="mobile-menu">
      <div v-if="isMenuOpen" class="mobile-menu" @click.self="toggleMobileMenu">
        <ul class="mobile-nav-items">
          <li
            v-for="(item, index) in links"
            :key="index"
            class="mobile-nav-item"
          >
            <div v-if="!item.children">
              <NuxtLink
                :to="item.path"
                class="mobile-nav-link"
                :class="{ 'active-link': activeIndex === index }"
                @click.native="
                  setActive(index);
                  toggleMobileMenu();
                "
              >
                {{ item.name }}
              </NuxtLink>
            </div>

            <div v-else class="mobile-dropdown-parent">
              <div
                class="mobile-nav-link"
                @click.stop="toggleDropdown(index)"
                :class="{ 'active-link': activeIndex === index }"
              >
                {{ item.name }}
                <span class="dropdown-arrow">▼</span>
              </div>

              <transition name="mobile-dropdown">
                <ul
                  v-if="dropdownOpenIndex === index"
                  class="mobile-dropdown-menu"
                >
                  <li
                    v-for="(child, childIndex) in item.children"
                    :key="childIndex"
                    class="mobile-dropdown-item"
                    @click.stop="setActiveChild(index, childIndex)"
                  >
                    <NuxtLink
                      :to="child.path"
                      class="mobile-dropdown-link"
                      :class="{
                        'active-link':
                          activeChildIndex === childIndex &&
                          activeIndex === index,
                      }"
                      @click.native="toggleMobileMenu()"
                    >
                      {{ child.name }}
                    </NuxtLink>
                  </li>
                </ul>
              </transition>
            </div>
          </li>

          <!-- Mobile Auth Links -->
          <li class="mobile-nav-item">
            <div v-if="!isLoggedIn" class="mobile-nav-link" @click="login">
              Login
            </div>
            <div v-else class="mobile-profile-section">
              <div class="mobile-profile-info">
                <img
                  :src="userProfile.avatar"
                  class="profile-avatar"
                  alt="Profile"
                />
                <span class="profile-name">{{ userProfile.name }}</span>
              </div>
              <div class="mobile-profile-actions">
                <div class="mobile-profile-link" @click="viewProfile">
                  <span>👤</span> Profile
                </div>
                <div class="mobile-profile-link" @click="logout">
                  <span>🚪</span> Logout
                </div>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </transition>
  </nav>
</template>

<script setup>
import { ref, watch } from "vue";
import { useRouter, useRoute } from "vue-router";

const router = useRouter();
const route = useRoute();

// Reactive state
const title = ref("X-Tweet");
const isMenuOpen = ref(false);
const activeIndex = ref(0);
const dropdownOpenIndex = ref(null);
const activeChildIndex = ref(0);
const isLoggedIn = ref(false);
const isProfileDropdownOpen = ref(false);
const userProfile = ref({
  name: "John Doe",
  email: "john@example.com",
  avatar:
    "https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp",
});

// Navigation items
const links = [
  { name: "Home", path: "/" },
  { name: "Trends", path: "/trendingTopics" },
  {
    name: "Analytics",
    children: [
      { name: "Search", path: "/search" },
      { name: "Tweets", path: "/tweets" },
      { name: "Sentiment", path: "/sentiment" },
      // { name: "Influencer Impact", path: "/Influencer" },
      { name: "Anomaly", path: "/anomaly" },
      { name: "Insights", path: "/AdvanceAnalysis" },
      

      // { name: "Compare", path: "/compare" },
      
    ],
  },
  { name: "About", path: "/about" },
];

// Route watcher
watch(
  () => route.path,
  (newPath) => {
    links.forEach((item, index) => {
      if (item.children) {
        const childIndex = item.children.findIndex(
          (child) => child.path === newPath
        );
        if (childIndex !== -1) {
          activeIndex.value = index;
          activeChildIndex.value = childIndex;
        }
      } else if (item.path === newPath) {
        activeIndex.value = index;
      }
    });
  }
);

// Methods
const setActive = (index) => {
  activeIndex.value = index;
  isMenuOpen.value = false;
};

const toggleMobileMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const toggleDropdown = (index) => {
  dropdownOpenIndex.value = dropdownOpenIndex.value === index ? null : index;
  if (dropdownOpenIndex.value === index) setActive(index);
};

const setActiveChild = (parentIndex, childIndex) => {
  activeIndex.value = parentIndex;
  activeChildIndex.value = childIndex;
  dropdownOpenIndex.value = null;
  isMenuOpen.value = false;
};

// Auth methods
const login = () => {
  isLoggedIn.value = true;
  isMenuOpen.value = false;
  // Implement actual login logic
};

const logout = () => {
  isLoggedIn.value = false;
  isProfileDropdownOpen.value = false;
  router.push("/");
};
const viewProfile = () => {
  router.push("/profile");
};
</script>

<style scoped>
/* Base Styles */
.navbar {
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: #171717;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.desktop-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 2rem;
  height: 64px;
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.logo {
  width: 40px;
  height: 40px;
}

.title {
  color: white;
  font-size: 1.5rem;
  margin: 0;
}

/* Navigation Items */
.nav-items {
  display: flex;
  gap: 1.5rem;
  list-style: none;
  margin: 0;
  padding: 0;
  flex-grow: 1;
  justify-content: center;
}

.nav-item {
  position: relative;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: white;
  text-decoration: none;
  padding: 0.75rem 1rem;
  border-radius: 6px;
  transition: all 0.2s ease;
  cursor: pointer;
}

.nav-link:hover {
  background: #ffffff15;
}

.active-link {
  background: #387ef0;
}

/* Dropdown Styles */
.dropdown-parent {
  position: relative;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  background: #2a2a2a;
  border-radius: 6px;
  padding: 0.5rem;
  min-width: 200px;
  list-style: none;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 1001;
}

.dropdown-item {
  padding: 0.25rem;
}

.dropdown-link {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  border-radius: 4px;
  color: white;
  text-decoration: none;
  cursor: pointer;
}

.dropdown-link:hover {
  background: #ffffff10;
}

/* Auth Styles */
.auth-links {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.login-button {
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 24px;
  background: #387ef0;
  cursor: pointer;
  transition: all 0.2s ease;
}

.login-button:hover {
  background: #2c6bc5;
}

.profile-dropdown {
  position: relative;
  cursor: pointer;
}

.profile-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 1rem;
  border-radius: 24px;
  background: #2a2a2a;
}

.profile-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
}

.profile-name {
  color: white;
  font-weight: 500;
  font-size: 0.9rem;
}

.profile-menu {
  right: 0;
  left: auto;
  min-width: 180px;
}

/* Mobile Styles */
/* Mobile Styles */
@media (max-width: 768px) {
  .desktop-nav {
    display: none;
  }

  .dropdown-menu {
    position: static;
    background: #1a1a1a;
    margin-top: 0.5rem;
  }
}

.mobile-nav {
  display: none;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  height: 64px;
}

.menu-toggle {
  background: none;
  border: none;
  color: white;
  font-size: 1.5rem;
  cursor: pointer;
}

.mobile-menu {
  position: fixed;
  top: 64px;
  left: 0;
  right: 0;
  background: #171717;
  padding: 1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-height: calc(100vh - 64px);
  overflow-y: auto;
  z-index: 1000;
}

.mobile-nav-items {
  list-style: none;
  padding: 0;
  margin: 0;
}

.mobile-nav-item {
  margin: 0.5rem 0;
}

.mobile-nav-link {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  color: white;
  text-decoration: none;
  border-radius: 6px;
}

.mobile-profile-section {
  padding: 1rem;
  border-top: 1px solid #3a3a3a;
}

.mobile-profile-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.mobile-profile-actions {
  padding-top: 1rem;
}

.mobile-profile-link {
  color: white;
  padding: 0.75rem;
  border-radius: 6px;
  transition: background 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.mobile-profile-link:hover {
  background: #ffffff10;
}

/* Transitions */
.dropdown-enter-active,
.dropdown-leave-active {
  transition: all 0.2s ease;
}

.dropdown-enter-from,
.dropdown-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: all 0.3s ease;
}

.mobile-menu-enter-from,
.mobile-menu-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

.mobile-dropdown-enter-active,
.mobile-dropdown-leave-active {
  transition: all 0.3s ease;
  max-height: 500px;
}

.mobile-dropdown-enter-from,
.mobile-dropdown-leave-to {
  opacity: 0;
  max-height: 0;
}

/* Responsive Design */
@media (max-width: 768px) {
  .desktop-nav {
    display: none;
  }

  .mobile-nav {
    display: flex;
  }
}
</style>
