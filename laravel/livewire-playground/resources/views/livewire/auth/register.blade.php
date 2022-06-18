<div class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
        <div>
            <img class="mx-auto h-32 w-auto" src="{{ asset('img/logo.svg') }}" alt="FriendGamesLogo">
            <p class="text-3xl text-center font-monofett">Novo Objetivo </p>
            <h2 class="mt-3 text-center text-3xl font-extrabold text-gray-900">
                Crie sua conta
            </h2>
            <p class="mt-2 text-center text-sm text-gray-600">
                Ou
                <a href="#" class="font-medium text-indigo-600 hover:text-indigo-500"> Faça login clicando aqui</a>
            </p>
        </div>
        <form wire:submit.prevent="register" class="mt-8 space-y-6">
            <input type="hidden" name="remember" value="true">

            <div class="rounded-md shadow-sm -space-y-px">
                
                {{-- email --}}
                <div class="pt-2">
                    <label class="block mb-1 @error('email') text-red-600 @enderror" for="email">Email</label>
                    <input wire:model="email" id="email" name="email" type="email" autocomplete="email" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm @error('email') border-red-600 @enderror" placeholder="Email">
                    @error('email')
                        <p class="mt-2 text-red-600 text-sm">
                            {{ $message }}
                        </p>
                    @enderror
                </div>
                
                {{-- password --}}
                <div class="pt-2">
                    <label class="block mb-1 @error('password') text-red-600 @enderror" for="password">Senha</label>
                    <input wire:model.lazy="password" id="password" name="password" type="password" autocomplete="current-password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm @error('password') border-red-600 @enderror" placeholder="Senha">
                    @error('password')
                        <p class="mt-2 text-pink-600 text-sm">
                            {{ $message }}
                        </p>
                    @enderror
                </div>
                
                {{-- passwordConfirmation--}}
                <div class="pt-2">
                    <label class="block mb-1 @error('passwordConfirmation') text-red-600 @enderror" for="passwordConfirmation">Confirme sua senha</label>
                    <input wire:model.lazy="passwordConfirmation" id="passwordConfirmation" name="passwordConfirmation" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm @error('passwordConfirmation') border-red-600 @enderror" placeholder="Confirme sua senha">
                    @error('passwordConfirmation')
                        <p class="mt-2 text-pink-600 text-sm">
                            {{ $message }}
                        </p>
                    @enderror
                </div>
            </div>

            {{-- Lembre me e Esqueci minha senha --}}
            <div class="flex items-center justify-between">
                <div class="flex items-center">
                    <input id="remember-me" name="remember-me" type="checkbox" class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded">
                    <label for="remember-me" class="ml-2 block text-sm text-gray-900"> Lembre-me </label>
                </div>

                <div class="text-sm">
                    <a href="#" class="font-medium text-indigo-600 hover:text-indigo-500"> Esqueceu sua senha? </a>
                </div>
            </div>

            {{-- Submit --}}
            <div>
                <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                        <!-- Heroicon name: solid/lock-closed -->
                        <svg class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                            <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
                        </svg>
                    </span>
                    Criar Conta
                </button>
            </div>

        </form>
    </div>
</div>




{{-- <div>
    <form wire:submit.prevent="register">
        <div>
            <label for="email">email</label>
            <input wire:model="email" type="text" id="email" name="email">
            @error('email') <span>{{ $message }}</span> @enderror

        </div>
        <div>
            <label for="password">password</label>
            <input wire:model="password" type="password" id="password" name="password">
            @error('password') <span>{{ $message }}</span> @enderror
        </div>
        <div>
            <label for="passwordConfirmation">passwordConfirmation</label>
            <input wire:model="passwordConfirmation" type="password" id="passwordConfirmation" name="passwordConfirmation">
            @error('passwordConfirmation') <span>{{ $message }}</span> @enderror
        </div>
        <div>
            <input type="submit" value="register">
        </div>
    </form>
</div> --}}
