<template>
        <v-app-bar :elevation="24" rounded>
        <template v-slot:append>
            <v-btn icon="mdi-heart"></v-btn>

            <v-btn icon="mdi-magnify"></v-btn>

            <v-btn icon="mdi-dots-vertical"></v-btn>
        </template>
        </v-app-bar>
        <!-- <v-app-bar> -->
            <!-- <NuxtLink to="/about">Фильтр</NuxtLink> -->
        <!-- </v-app-bar> -->
        
    <div>
        <h1>Домашняя страница</h1>
        
    </div>
    <div v-for="product in products" :key="product.id">
        <v-card>
            <v-img :src="URL_BACK+product.img" height="180px"></v-img>
            <v-card-title>{{ product.title }}</v-card-title>
            <v-card-text>{{ product.text }}</v-card-text>
            <v-card-actions>
                <v-btn variant="flat" color="indigo" >
                    Купить
                </v-btn>
            </v-card-actions>
        </v-card>
    </div>

</template>

<script setup>
const URL_BACK = 'http://127.0.0.1:8000'
const {data:products} = await useFetch('http://127.0.0.1:8000/api/v1')
</script>

<style scoped>

</style>
