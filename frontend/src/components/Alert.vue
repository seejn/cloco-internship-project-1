<template>
    <div class="m-auto w-1/2 border-t-4  p-4  shadow-md relative " :class="alertClassObject" role="alert">
        <p class="font-bold">Tailwindcss working</p> 
        <p>Make Something Great !!!</p> 
        <p class="absolute top-0 right-0 px-4 py-3 text-2xl font-bold cursor-pointer">&times;</p>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                isError: false
            }
        },
        computed: {
            alertClassObject() {
                return {
                "text-green-700": !this.isError,
                "bg-green-100": !this.isError,
                "border-green-700": !this.isError,
                
                "text-red-700": this.isError,
                "bg-red-100": this.isError,
                "border-red-700": this.isError,
                }
            }
        }
    }
</script>