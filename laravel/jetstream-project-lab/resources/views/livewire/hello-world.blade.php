<div>
    <div class="container">
        <div class="flex">
            <div class="col-6 mx-auto py-3 bg-red-700 h-full">
                <input wire:model.lazy="message" type="text">
            </div>
            <div class="col-6 mx-auto py-3 bg-gray-50">
                <h1>{{ $message }}</h1>
            </div>
        </div>
    </div>
</div>
