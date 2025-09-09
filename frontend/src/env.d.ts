declare namespace NodeJS {
  interface ProcessEnv {
    NODE_ENV: string;
    VUE_ROUTER_MODE: 'hash' | 'history' | 'abstract' | undefined;
    VUE_ROUTER_BASE: string | undefined;
  }
}

declare module '#q-app/wrappers' {
  import type { BootCallback } from '@quasar/app-vite';
  export { BootCallback };
}

declare module '*.vue' {
  import type { DefineComponent } from 'vue';
  const component: DefineComponent<Record<string, unknown>, Record<string, unknown>, unknown>;
  export default component;
}

// Quasar specific types
declare module 'quasar' {
  interface Quasar {
    // Add Quasar specific types if needed
  }
}

// Vue shims for Quasar
declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $q: unknown; // Use a more specific type if available
  }
}