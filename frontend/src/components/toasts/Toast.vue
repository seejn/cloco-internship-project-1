<template>
    <div :class="toastClassObject"  style="z-index: 1;" class="relative mt-4 w-full border-t-4  p-4  shadow-md " role="alert">
        <p class="font-bold">{{ toast.title }}</p> 
        <p>{{ toast.message }}</p> 
        <p @click="dismissToast" class="absolute top-0 right-0 px-4 py-3 text-2xl font-bold cursor-pointer">&times;</p>
    </div>
</template>

<script>
    export default {
        props: {
            toast: {
                required: true,
                type: Object,
            }
        },
        
        created() {
            setTimeout(() => {
               this.dismissToast() 
            }, 4000);

        },
        methods: {
            dismissToast() {
                this.$store.commit("clearToast", this.toast)
            }
        },computed: {
            toastClassObject() {
                return {
                "text-green-700": !this.toast.isError,
                "bg-green-100": !this.toast.isError,
                "border-green-700": !this.toast.isError,
                
                "text-red-700": this.toast.isError,
                "bg-red-100": this.toast.isError,
                "border-red-700": this.toast.isError,
                }
            }
        }
    }
</script>