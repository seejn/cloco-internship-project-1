<template>
    <h3 class="text-lg font-semibold text-gray-900">Personal Information</h3>
    <ul class="mt-4 space-y-4">
        <li class="flex items-center">
            <span class="font-semibold text-gray-700 w-32">Email:</span>
            <span class="text-gray-600">{{ user.email }}</span>
        </li>
        <li class="flex items-center">
            <span class="font-semibold text-gray-700 w-32">Contact:</span>
            <span class="text-gray-600">{{ user.contact }}</span>
        </li>
        <li class="flex items-center">
            <span class="font-semibold text-gray-700 w-32">Address:</span>
            <span class="text-gray-600">{{ user.address }}</span>
        </li>
    </ul>
</template>
<script>
    export default {
        props: {
            user: {
                type: Object,
                required: true
            }
        }
    }
</script>