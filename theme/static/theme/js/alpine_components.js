function multiselect({ name }) {
    return {
        multiselect_open: false,
        selected: [],
        get selectedIds() {
            return this.selected.map(item => item.id.toString());
        },
        toggle(option) {
            const index = this.selected.findIndex(item => item.id === option.id);
            if (index === -1) {
                this.selected.push(option);
            } else {
                this.selected.splice(index, 1);
            }
        },
        name: name,
    };
}
