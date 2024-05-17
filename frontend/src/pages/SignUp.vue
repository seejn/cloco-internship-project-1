<template>
    <Toasts />
    <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-sm">
            <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Welcome</h2>
        </div>

        <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
            <form class="space-y-6" @submit.prevent="signUp">
            <div>
                <label :class="{'text-red-600': !emailValidState.state}" for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
                <div class="mt-2">
                <input @blur="isEmailValid" :class="{'ring-red-600': !emailValidState.state}" v-model="input.email"  id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 px-1 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">

                <span v-if="!emailValidState.state">
                    <p class="text-red-600 text-sm">{{ emailValidState.message }}</p>
                </span>

                </div>
            </div>

            <div>
                <div class="flex items-center justify-between">
                    <label :class="{'text-red-600': !passwordValidState.state}" for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
              
                </div>
                <div class="mt-2">
                    <input @blur="isPasswordValid" :class="{'ring-red-600': !passwordValidState.state}" v-model="input.password" id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 px-1 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    <span v-if="!passwordValidState.state">
                        <p class="text-red-600 text-sm">{{ passwordValidState.message }}</p>
                    </span>
                </div>
            </div>

            <div>
                <div class="flex items-center justify-between">
                    <label :class="{'text-red-600': !cPasswordValidState.state}" for="password" class="block text-sm font-medium leading-6 text-gray-900">Confirm Password</label>
              
                </div>
                <div class="mt-2">
                    <input @blur="doesPasswordsMatch" :class="{'ring-red-600': !cPasswordValidState}" v-model="input.cpassword" id="cpassword" name="cpassword" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 px-1 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    <span v-if="!cPasswordValidState.state">
                        <p class="text-red-600 text-sm">{{ cPasswordValidState.message }}</p>
                    </span>
                </div>
            </div>

            <div>
                <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign Up</button>
            </div>
            </form>

            <p class="mt-10 text-center text-sm text-gray-500">
            Already a member?
            <RouterLink to="/signin" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Login Here</RouterLink>
            </p>
            
            <p class="mt-10 text-center text-sm text-gray-500">
            <RouterLink to="/" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Go back</RouterLink>
            </p>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        components: {
        },
        data() {
            return {
                input: {
                    email: '',
                    password: '',
                    cpassword: '',
                },
                emailValidState: {
                    state: true,
                    message: ''
                },
                passwordValidState: {
                    state: true,
                    message: ''
                },
                cPasswordValidState: {
                    state: true,
                    message: ''
                },
            }
        },
        methods: {
            isEmailValid() {
                if(this.input.email === ""){
                    this.emailValidState.state = false
                    this.emailValidState.message = "This field is required"
                    return false
                }

                const emailregex = /^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/g
                if(!emailregex.test(this.input.email)){
                    this.emailValidState.state = false
                    this.emailValidState.message = "Email not valid"
                    return false
                }

                this.emailValidState.state = true

                return true
            },
            isPasswordValid() {
                if(this.input.password === ""){
                    this.passwordValidState.state = false
                    this.passwordValidState.message = "This field is required"
                    return false
                }

                const passwordregex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/
                if(!passwordregex.test(this.input.password)){
                    this.passwordValidState.state = false
                    this.passwordValidState.message = "Password must be 8+ characters with uppercase, lowercase, number, and special character"
                    return false
                }

                this.passwordValidState.state = true
                return true
            },
            doesPasswordsMatch() {
                if(this.input.cpassword === ""){
                    this.cPasswordValidState.state = false
                    this.cPasswordValidState.message = "This field is required"
                    return false
                }
                if(this.input.password !== this.input.cpassword){
                    this.cPasswordValidState.state = false
                    this.cPasswordValidState.message = "Passwords does not match"
                    return false
                }
                this.cPasswordValidState.state = true
                return true
            },
            resetFields() {
                this.input.email = ""
                this.input.password = ""
                this.input.cpassword = ""
            },
            async signUp() {
                
                if(!this.isEmailValid()) return 

                if(!this.isPasswordValid()) return 

                if(!this.doesPasswordsMatch()) return 

                await axios(`${import.meta.env.VITE_BASE_URL}/user/register/`,{
                    method: 'post',
                    headers: {
                        "Content-Type": "application/json"
                    },
                    data: {
                        "email": this.input.email,
                        "password": this.input.password,
                    }
                })
                .then((response) => {
                    console.log(response.status)
                    this.$store.commit("addToast", {
                        title: response.statusText,
                        isError: false,
                        message: response.data.message
                    })
                    if(response.status == 201) this.$router.push('/signin')
                })
                .catch((error) => {
                    this.resetFields()
                    console.log(error.response.statusText)
                    console.log(error.response.data.message)
                    this.$store.commit("addToast", {
                        title: error.response.statusText,
                        isError: true,
                        message: error.response.data.message
                    })
                })
            }
        }, 
    }
</script>
<style></style>