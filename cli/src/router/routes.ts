import type { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('../modules/front-facing/hero/HeroPage.vue'),
  },
  {
    path: '/login',
    component: () => import('../modules/auth/LoginPage.vue'),
  },
  {
    path: '/signup',
    component: () => import('../modules/auth/SignupPage.vue'),
  },
  {
    path: '/dashboard',
    component: () => import('layouts/DashboardLayout.vue'),
    children: [
      { path: '/', component: () => import('../modules/home/HomePage.vue') }
    ],
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('../modules/error/NotFoundPage.vue'),
  },
];

export default routes;
