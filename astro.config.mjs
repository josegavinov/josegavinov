// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
	site: 'https://josegavinov.github.io',
	// El repo se llama `josegavinov`, así que GitHub Pages lo sirve bajo ese
	// subdirectorio. Si mueves el sitio a un repo `josegavinov.github.io`,
	// borra esta línea para que quede en la raíz del dominio.
	base: '/josegavinov',
});
