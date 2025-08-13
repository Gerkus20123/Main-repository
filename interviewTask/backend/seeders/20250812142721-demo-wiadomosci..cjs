'use strict';

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.bulkInsert('Wiadomosci', [{
      content: 'Pierwsza przykładowa wiadomość!',
      createdAt: new Date(),
      updatedAt: new Date()
    }, {
      content: 'To jest druga wiadomość dodana przez seeder.',
      createdAt: new Date(),
      updatedAt: new Date()
    }, {
      content: 'I ostatnia, trzecia wiadomość od seedera.',
      createdAt: new Date(),
      updatedAt: new Date()
    }], {});
  },

  async down(queryInterface, Sequelize) {
    await queryInterface.bulkDelete('Wiadomosci', null, {});
  }
};