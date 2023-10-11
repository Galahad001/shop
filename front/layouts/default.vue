<template>
    <v-app>
        <header>
            <v-app-bar
            app
            color="grey"
            >
            <v-app-bar-title>
                <h3>iTEST</h3>
                <v-btn  flat to="/">Домой</v-btn>
                <v-btn  flat to="/about">О нас</v-btn>
                <v-btn class="mr-4" variant="plain" to="/products">Каталог</v-btn>
                
                <v-btn to="/basket" class="text-none" stacked>
                    <v-badge  :content="basketStore.productsTotal" color="error">
                        <v-icon>mdi-cart-outline</v-icon>
                    </v-badge>
                </v-btn>

            </v-app-bar-title>

            </v-app-bar>
        </header>

        <v-main class="cont">
            <slot/>
        </v-main>

        <v-footer class="b" :elevation="20" rounded>
            <v-row justify="center" no-gutters>
                <v-btn
                    v-for="link in links"
                    :key="link.name"
                    variant="text"
                    class="mx-2"
                    rounded="xl"
                    :to=link.href
                >
                    {{ link.name }}
                </v-btn>
                <v-col class="text-center mt-4" cols="12">
                    {{ new Date().getFullYear() }} — <strong>Xiver</strong>
                </v-col>
            </v-row>

        </v-footer>
    </v-app>
    
</template>

<script setup>
const basketStore = useBasketStore()

const links = [
    { name: 'Главная', href: '/' },
    { name: 'О нас', href: '/about' },
    { name: 'Каталог', href: '/products' },
]
</script>

<style  scoped>
.v-container{
    display: flex;
}
.text-decoration-none {
  color: grey;
}

.router-link-exact-active {
  color: #12b488;
}

footer{
   max-height: 100px;
}
</style>