
<form wire:submit.prevent="save">
    <input type="text" wire:model="post.title">
    <textarea wire:model="post.content"></textarea>
    <button type="submit">Save</button>
</form>
