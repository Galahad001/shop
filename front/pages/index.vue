<template>
    <v-container>
        <div>
            <h1>Домашняя страница</h1>
        </div>
        <v-col v-for="product in products" :key="product.id" sm="4" md="3" class="card_line">
            <ProductCard :product="product" />
        </v-col>
    </v-container>

</template>

<script setup>

const {data:products} = await useFetch('http://127.0.0.1:8000/api/v1')
import ProductCard from '~~/components/ProductCard.vue'
</script>

<style scoped>
.card_line{
    display: inline-block;
}
</style>
