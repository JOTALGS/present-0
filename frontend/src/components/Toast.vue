<script setup>
import { useToastStore } from '@/stores/toast';

const store = useToastStore()

</script>

<template>
  <div
    v-if="store.isVisible"
    class="transition ease-in-out delay-500 duration500 px-6 py-6 fixed top-full right-8 rouded-lg"
    :class="store.classes"
  >
    {{ store.message }}
  </div>
</template>
