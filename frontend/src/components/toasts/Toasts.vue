<template>
  <div v-if="toasts.length" class="w-1/3 absolute right-2 ">
    <Toast
      v-for="toast of toasts"
      :toast="toast">
    </Toast>
  </div>
</template>
  
<script>
  import Toast from './Toast.vue'
  
  export default {
    components: { 
        Toast 
    },
    computed: {
      toasts() {
        return this.$store.state.toasts;
      }
    }
  }
</script>